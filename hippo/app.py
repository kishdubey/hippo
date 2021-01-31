from flask import Flask, render_template, url_for, request

from chatbot import bot

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

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    emotion_used = False
    if _find_subwords(userText, "tips"):
        return 'Here are some resources that can help, https://www.ottawapublichealth.ca/en/public-health-topics/mental-health.aspx'
    elif userText.lower() == 'bye' or _find_subwords(userText.lower(), "bye"):
            return "Bye, I'm always here if you need me"
    elif emotion_used or userText.lower() == "hello" or userText.lower() == "hi":
        return str(bot.get_response(userText))
    elif not emotion_used:
        emotion_used = True
        emotion = predict(userText, model, tokenizer)
        response = f"Ah, I see you are feeling {emotion}. Would you like to tell me more?"
        return response

@app.route("/mood")
def mood():
    return render_template("mood.html")

def _find_subwords(str, target):
    li = str.split(" ")
    for word in li:
        if word == target:
            return True

    return False

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
    return ans

if __name__ == "__main__":
    app.run(debug=True)
