import wikipedia
from Speak import *

def Wikipedia(search):
    result = wikipedia.summary(search, sentences = 2)
    speak(result)
    