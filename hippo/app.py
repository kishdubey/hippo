from flask import Flask, render_template, url_for

#from chatbot import bot

import keras
from  keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hippo.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

def _setup_models(TOKENIZER_PATH, MODEL_PATH):
    """
    Setting up model and tokenizer
    """
    with open(TOKENIZER_PATH, 'rb') as handle:
        tokenizer = pickle.load(handle)
    model = keras.models.load_model(MODEL_PATH)
    return tokenizer, model

MODEL_PATH = "classification_model/model.h5"
TOKENIZER_PATH =  "classification_model/tokenizer.pickle"
tokenizer, model = _setup_models(TOKENIZER_PATH, MODEL_PATH)

def _get_key(value):
    """
    (integer) -> string
    Returning emotion associated with value
    """
    dict={'joy':0,'anger':1,'love':2,'sadness':3,'fear':4,'surprise':5}
    for key, val in dict.items():
        if (val==value):
            return key

def predict(sentence, model, tokenizer):
    """
    (string) -> emotion
    Predicting emotion of provided text
    """
    sentence_lst=[]
    sentence_lst.append(sentence)
    sentence_seq=tokenizer.texts_to_sequences(sentence_lst)
    sentence_padded=pad_sequences(sentence_seq,maxlen=80,padding='post')
    ans=_get_key(model.predict_classes(sentence_padded))
    return "The emotion predicted is", ans

if __name__ == "__main__":
    app.run(debug=True)
