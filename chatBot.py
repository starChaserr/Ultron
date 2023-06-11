from pyexpat import model
import random
import json
import re
import numpy as np
import pickle

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def cleaner(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bagger(sentence):
    sentence_words = cleaner(sentence)
    bag = [0]* len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predictor(sentence):
    wordBank = bagger(sentence)
    res = model.predict(np.array([wordBank]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]
    result.sort(key=lambda x: x[1], reverse = True)
    return_list = []
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability':str(r[1])})
    return return_list

def response(intent_list, intents_json):
    tag = intent_list[0]['intent']
    intentList = intents_json['intents']
    for i in intentList:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def responder(message):
    return response(predictor(message), intents)