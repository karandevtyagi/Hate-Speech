
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer
import re
from keras.preprocessing.sequence import pad_sequences
from textblob import TextBlob
import tensorflow as tf
import numpy as np
import pickle
import tweepy
from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
cors = CORS(app)
# Consumer keys and access tokens, used for OAuth


def getWorldCloud(words):
    SampleTextInBlobFormat = TextBlob(words)
    NounPhrases = SampleTextInBlobFormat.noun_phrases
    NewNounList = []
    for words in NounPhrases:
        for x in words.split():
            NewNounList.append(x)
    return NewNounList


def get_tweets(username):
    tmp = []
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    tweets = api.user_timeline(
        screen_name=username, count=200, include_rts=False)
    for i in tweets:
        name = (i.user.name)
        screenName = (i.user.screen_name)
        image_url = (i.user.profile_image_url)
        break
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    return dict(name=name, screenName=screenName, image=image_url, all_tweets=tmp)


# cleaning text of training labelled dataset
# to return processed tweets
def Process(model, tokenizer, userData):
    corpus = []
    corpus2 = []
    tmp = userData['all_tweets']
    train_len = len(tmp)
    for i in range(0, train_len):
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
        tweet = re.sub('[^a-zA-Z]', ' ', tweet)

        # Replace multiple spaces with a single space
        tweet = re.sub(r'\s+', ' ', tweet)

        tweet = tweet.split()
        corpus2.append(tweet)

        # lemmatizing data for better meaning of words in corpus
        lemmatizer = WordNetLemmatizer()
        tweet = [lemmatizer.lemmatize(word) for word in tweet if not word in set(
            stopwords.words('english'))]
        tweet = ' '.join(tweet)
        corpus.append(tweet)

    vocab_size = 1000
    max_length = 50
    tokenizer1 = Tokenizer(num_words=vocab_size)
    tokenizer1.fit_on_texts(corpus)

    sequences = tokenizer.texts_to_sequences(corpus)
    X = pad_sequences(sequences, maxlen=max_length)

    # prediction
    X_test = X
    batch_size = 10
    y_pred = model.predict(X_test, batch_size=batch_size, verbose=1)
    y_pred = (y_pred > 0.5)
    y_pred = y_pred*1
    hate = []
    hate_word = ''
    offensive_word = ''
    for i in range(len(y_pred)):
        if(y_pred[i][0] == 1):
            hate.append(tmp[i])
            hate_word = hate_word+corpus[i]+" "
    hate_words = getWorldCloud(hate_word)
    offensive = []
    for i in range(len(y_pred)):
        if(y_pred[i][1] == 1):
            offensive.append(tmp[i])
            offensive_word = offensive_word+corpus[i]+" "
    offensive_words = getWorldCloud(offensive_word)
    h = (y_pred[:, 0] == 1).sum()
    o = (y_pred[:, 1] == 1).sum()
    c = (y_pred[:, 2] == 1).sum()
    # most used words
    most_used_words = []
    for word, i in tokenizer1.word_index.items():
        most_used_words.append(word)
    return (dict(h=str(h), o=str(o), c=str(c), hate_words=hate_words, offensive_words=offensive_words, most_used_words=most_used_words, hate_tweets=hate, offensive_tweets=offensive, userimage=userData['image'], username=userData['name'], userscreenanme=userData['screenName']))


# api
@app.route('/user', methods=['POST'])
def extractTweets():
    model = tf.keras.models.load_model('trained_model.h5')
    f1 = open(r"model4.pkl", "rb")
    tokenizer = pickle.load(f1)

    req_data = request.get_json()
    username = req_data['username']
    userData = get_tweets(username)
    return Process(model, tokenizer, userData)
