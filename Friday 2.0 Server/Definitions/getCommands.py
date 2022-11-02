import speech_recognition as sr #pip install SpeechRecognition
from Basic import *


def takeCMD():
    query = input()
    return query

def takeMic(conn):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-CA")
        except Exception as e:
            return "null", True
        else:
            connection = mySpeech(conn, query)


        return query, connection