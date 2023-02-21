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

lemmatizer = WordNetLemmatizer()
punct = dict((ord(i), None) for i in string.punctuation)

def tokenize():
    file = open('rentalAgreement.txt', 'r', errors='ignore')
    rentalAgreement = file.read()
    sentence_tokens = nltk.sent_tokenize(rentalAgreement)
    word_tokens = nltk.word_tokenize(rentalAgreement)
    return sentence_tokens, word_tokens

def lemtokens(tokens):
    list=[] 
    for i in tokens:
        list.append(lemmatizer.lemmatize(i))
    return list

def lemmer(text):
    tokenized_text = nltk.word_tokenize(text.lower().translate(punct))
    lemmatized_values = lemtokens(tokenized_text)
    return lemmatized_values


greeting_inputs = ['hello', 'hi', 'hey', 'greetings']
greeting_responses = ['hi, I am a chatbot']

def greeting(text):
    for token in text.split():
        if token.lower() in greeting_inputs:
            return greeting_responses[0]
        
def respond(user_query):
    bot_response = ""
    
    #Tokenize
    sent_tokens, word_tokens = tokenize()
    sent_tokens.append(user_query)
    tfidf_obj = TfidfVectorizer(tokenizer=lemmer, stop_words="english")
    tfidf = tfidf_obj.fit_transform(sent_tokens)
    
    # cosine similarity the last element with the entire list 
    sim_values = cosine_similarity(tfidf[-1], tfidf) 
    
    print(sim_values)
    
    # selecting the reponse or token with the max similarity
    #index = sim_values.argsort()[0][-3]
    index = sim_values.argsort()[0]
    print(index)
    #index = 11
    
    flattened_sim = sim_values.flatten()
    flattened_sim.sort()
    print(flattened_sim)
    
    for i in range (len(flattened_sim)):
        print("Loop:",i)
        if (flattened_sim[-2-i] == 0 or len(bot_response.split())>50):
            break
        else:
            bot_response += sent_tokens[index[-2-i]]
            
    if bot_response == "":
        return "I cannot understand"
    else:
        return bot_response
    
    # required_tfidf = flattened_sim[-2]
    
    # if(required_tfidf == 0):
    #     bot_response += "I cannot understand"
    #     return bot_response
    # else: 
    #     bot_response += bot_response + sent_tokens[index]
    #     return bot_response
    


flag = 1
print("Input a message to chatbot: \n")
while(flag == 1):
    user_query = input()
    user_query = user_query.lower()
    
    if (user_query == 'exit'):
        flag = 0
        print('Bot: Goodbye')
    else:
        if (greeting(user_query) != None):
            print("Bot: "+greeting(user_query))
            
        else:
            res = respond(user_query)
            print("Bot: ", res)
        
#print(greeting("hey"))
#print(tokenize())
#print(lemmer("apple@ is a good fruit!!!!"))

