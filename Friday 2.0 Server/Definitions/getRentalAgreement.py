import json
from Basic import *
from getCommands import takeMic

import nltk
from nltk.stem import WordNetLemmatizer 
import random
import string
import numpy as np
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')



def rentalAgreement(query, conn):
    flag = 0
    speak(conn, "What would you like to know about?")
    user_query, connection = takeMic(conn)
    user_query = user_query.lower()

    while True:
        if (user_query != ''):
            flag = 0
            res = respond(user_query)
            speak(conn, res)
        else:
            falg += 1
            if flag == 2:
                break
            speak(conn, "Sorry, I couldn't hear you")

        speak(conn, "Would you like to know about anything else?")
        user_query, connection = takeMic(conn)
        user_query = user_query.lower()
        if 'no' in user_query.split():
            print("It will now break")
            break
        else:
            continue

def respond(user_query):
    bot_response = ""
    #Tokenize
    sent_tokens = tokenize()
    sent_tokens.append(user_query)
    # Simplifies the text
    tfidf_obj = TfidfVectorizer(tokenizer=lemmer, stop_words="english")
    tfidf = tfidf_obj.fit_transform(sent_tokens)
    # cosine similarity the last element with the entire list 
    sim_values = cosine_similarity(tfidf[-1], tfidf) 
    # selecting the reponse or token with the max similarity
    index = sim_values.argsort()[0] # This gives an array with the indexes from lowest to highest of sentence placement in text
    # Flattening and sorting values 
    flattened_sim = sim_values.flatten()
    flattened_sim.sort() # This gives an array with values of how similar the senetnce is from lowest to highest
    # Will put the sentence with correlation to the question in the response
    for i in range (len(flattened_sim)):
        if (flattened_sim[-2-i] == 0 or len(bot_response.split())>50):
            break
        else:
            bot_response = bot_response + " " + sent_tokens[index[-2-i]]
    #Returns response        
    if bot_response == "":
        return "I don't have the answer to that question"
    else:
        return bot_response

def tokenize():
    # This function opens the rental agreement and converts the text to tokens
    file = open('.././Information/rentalAgreement.txt', 'r', errors='ignore')
    rentalAgreement = file.read()
    sentence_tokens = nltk.sent_tokenize(rentalAgreement)
    # word_tokens = nltk.word_tokenize(rentalAgreement)
    # return sentence_tokens, word_tokens
    return sentence_tokens
def lemmer(text):
    punct = dict((ord(i), None) for i in string.punctuation)
    tokenized_text = nltk.word_tokenize(text.lower().translate(punct))
    lemmatized_values = lemtokens(tokenized_text)
    return lemmatized_values
def lemtokens(tokens):
    lemmatizer = WordNetLemmatizer()
    list=[] 
    for i in tokens:
        list.append(lemmatizer.lemmatize(i))
    return list



















def rentalAgreementOLD(query, conn):
    with open('.././Information/public.json') as public:
        publicData = json.load(public)

    queryArray = query.split(" ")
    result = ""
    for i in range (len(queryArray)):
        sentence = ""
        for j in range(i, len(queryArray)):
            if i==j:
                sentence = queryArray[j]
            else:
                sentence = " ".join([sentence, queryArray[j]])

            if sentence in publicData:
                result = sentence

        if result != "":
            speak(conn, ("The "+ result+ " is " + publicData[result]))
            break