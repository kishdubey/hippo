import numpy as np
import keras
from  keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM,Bidirectional,Dense,Embedding,Dropout
import pickle

MODEL_PATH = "classification_model/model.h5"
TOKENIZER_PATH =  "classification_model/tokenizer.pickle"

with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model(MODEL_PATH)

def get_key(value):
    dict={'joy':0,'anger':1,'love':2,'sadness':3,'fear':4,'surprise':5}
    for key, val in dict.items():
        if (val==value):
            return key

def predict(sentence):
    sentence_lst=[]
    sentence_lst.append(sentence)
    sentence_seq=tokenizer.texts_to_sequences(sentence_lst)
    sentence_padded=pad_sequences(sentence_seq,maxlen=80,padding='post')
    ans=get_key(model.predict_classes(sentence_padded))
    return "The emotion predicted is", ans

print(predict("I was totally surprised by that"))
