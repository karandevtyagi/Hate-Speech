

#Importing the Libraries
import numpy as np
import pandas as pd



#loading dataset
dataset = pd.read_csv('labeled_data.txt', delimiter = '\t')
dataset2 = pd.read_csv('hate_speech_with_sentiment.txt', delimiter = ',', encoding = "ISO-8859-1")

#cleaning text of training labelled dataset 
import re
import nltk
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
corpus = []
corpus2=[]
train_len = 24000
for i in range(0,train_len):
    tweet = dataset['tweet'][i]
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
    
    



#cleaning text of training labelled dataset 
train_len = 16000
for i in range(0,train_len):
    tweet = dataset2['Tweets'][i]
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
    







y= dataset.iloc[0:24000,5].values;

for i in range(0,16000):
    if dataset2['Class'][i] == 'none':
         y =np.append(y,2)

    else:
        y=np.append(y,0)


vocab_size = 1500
max_length = 50
batch_size = 10
epochs = 6
emb_dim = 300




from keras.preprocessing.text import Tokenizer    
tokenizer = Tokenizer(num_words= vocab_size)
tokenizer.fit_on_texts(corpus)

from keras.preprocessing.sequence import pad_sequences
sequences = tokenizer.texts_to_sequences(corpus)
X = pad_sequences(sequences, maxlen=max_length)



#embeddings

embeddings_index = dict()
f = open('wiki-news-300d-1M.vec')
for line in f:
    values = line.rstrip().rsplit(' ')
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()
print('Loaded %s word vectors.' % len(embeddings_index))




# weight matrix
embedding_matrix = np.zeros((vocab_size, emb_dim))
for word, index in tokenizer.word_index.items():
    if index > vocab_size - 1:
        break
    else:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[index] = embedding_vector



y = y.reshape(-1,1)

from sklearn.preprocessing import OneHotEncoder
onehotencoder1 = OneHotEncoder()
Z = onehotencoder1.fit_transform(y).toarray()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Z,test_size = 0.2, random_state = 42)



most_used_words = []
for word, i in tokenizer.word_index.items():
    most_used_words.append(word)




from keras.models import Sequential
from keras.layers import Conv1D,MaxPooling1D,Dropout,Flatten,Activation,Dense,LSTM
from keras.layers.embeddings import Embedding
from keras import optimizers




#lstm + cnn

classifier = Sequential()
classifier.add(Embedding(vocab_size, emb_dim, input_length=50, weights=[embedding_matrix], trainable=True))
classifier.add(Dropout(0.2))
classifier.add(Conv1D(128, 3, activation='relu'))
classifier.add(MaxPooling1D(pool_size=4))
classifier.add(LSTM(128))
classifier.add(Dense(3, activation='softmax'))
classifier.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])    


classifier.fit(X_train, np.array(y_train),batch_size = batch_size, epochs = epochs,validation_data = (X_test,y_test), verbose = 1)


#lstm+cnn val acc = 91.42 epoch = 3 batch = 10 lstm(128)


import pickle
with open (r"model3.pkl", "wb") as output_file:
	pickle.dump(classifier, output_file)
	
with open(r"model3.pkl", "rb") as input_file:
	e = pickle.load(input_file)
	print(e)
with open (r"model4.pkl", "wb") as output_file:
	pickle.dump(tokenizer, output_file)
	
with open(r"model4.pkl", "rb") as input_file:
	e = pickle.load(input_file)
	print(e)
