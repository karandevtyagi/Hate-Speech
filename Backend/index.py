from flask import Flask,request,jsonify
app = Flask(__name__)
from flask_cors import CORS
cors = CORS(app)
import tweepy
import pickle
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer    
from keras.preprocessing.sequence import pad_sequences
# Consumer keys and access tokens, used for OAuth

def get_tweets(username):
	tmp=[]
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''

	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name=username, count=180)
	for i in tweets:
		name=(i.user.name)
		screenName=(i.user.screen_name)
		image_url=(i.user.profile_image_url)
		break
	tweets_for_csv = [tweet.text for tweet in tweets]
	for j in tweets_for_csv: 
		tmp.append(j)
	return dict(name=name,screenName=screenName,image=image_url,tmp=tmp)

#cleaning text of training labelled dataset 
import re
import nltk
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
#to return processed tweets
def Process(model,tokenizer,tmp):
	corpus = []
	corpus2=[]
	train_len = len(tmp)
	for i in range(0,train_len):
	    tweet = tmp[i]
	    tweet = tweet.lower()
	    # Replaces URLs with the word URL
	    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' ',  tweet)
	    
	    # Replace @handle with the word USER_MENTION
	    tweet = re.sub(r'@[\S]+', ' ', tweet)
	    
	    # Replaces #hashtag with hashtag
	    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
	    
	    # Remove RT (retweet)
	    tweet = re.sub(r'\brt\b', ' ', tweet)
	    
	    # Replace 2+ dots with space
	    tweet = re.sub(r'\.{2,}', ' ', tweet)
	    
	    # Strip space, " and ' from tweet
	    tweet = tweet.strip(' "\'')
	    
		# Replace other punctuations and numbers
	    tweet = re.sub('[^a-zA-Z]',' ', tweet)
	    
	    # Replace multiple spaces with a single space
	    tweet = re.sub(r'\s+', ' ', tweet)
	    
	    
	    
	    
	    tweet = tweet.split()
	    corpus2.append(tweet)
    

	    #lemmatizing data for better meaning of words in corpus 
	    lemmatizer = WordNetLemmatizer()
	    tweet = [lemmatizer.lemmatize(word) for word in tweet if not word in set(stopwords.words('english'))]
	    tweet = ' '.join(tweet)
	    corpus.append(tweet)
	    print(i," of ",train_len)
 
	vocab_size = 1000
	max_length = 50	
	tokenizer1 = Tokenizer(num_words= vocab_size)
	tokenizer1.fit_on_texts(corpus)

	sequences = tokenizer.texts_to_sequences(corpus)
	X = pad_sequences(sequences, maxlen=max_length)

	#most used words
	most_used_words = []
	for word, i in tokenizer1.word_index.items():
    		most_used_words.append(word)

	
	#prediction
	X_test = X
	batch_size = 10
	y_pred = model.predict(X_test, batch_size=batch_size, verbose = 1)
	y_pred=(y_pred>0.5)
	y_pred=y_pred*1
	print(type(y_pred))
	hate=[]
	for i in range(len(y_pred)):
	    	    if(y_pred[i][0]==1):
	    	    	    hate.append(tmp[i])
	offensive=[]
	for i in range(len(y_pred)):
	    	    if(y_pred[i][1]==1):
	    	    	    offensive.append(tmp[i])
	h=(y_pred[:,0]==1).sum() 
	o=(y_pred[:,1]==1).sum() 
	c=(y_pred[:,2]==1).sum()
	print(hate)
	#hscore
	hscore = (h+o)*100/(h+o+c) 
	return (dict(h=str(h),o=str(o),c=str(c),hscore=str(hscore),word=most_used_words,hate=hate,offensive=offensive))


#api
@app.route('/user',methods=['POST'])
def extractTweets():
	f = open(r"model3.pkl", "rb")
	model = pickle.load(f)
	f1 = open(r"model4.pkl", "rb")
	tokenizer = pickle.load(f1)
	global graph
	#graph = tf.compat.v1.get_default_graph
	graph = tf.get_default_graph()
	with graph.as_default():
		req_data=request.get_json() 
		username=req_data['username'] 
		userData=get_tweets(username) 
		result=Process(model,tokenizer,userData['tmp'])
		 
		
	return dict(userimage=userData['image'],username=userData['name'],userscreenanme=userData['screenName'],result=result)


