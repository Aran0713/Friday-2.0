import speech_recognition as sr #pip install SpeechRecognition
from Basic import *


def takeCMD():
    query = input()
    return query

def takeMic(conn):
    query = ""
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-CA")
            print(query)
        except Exception as e:
            return "", True
        else:
            connection = mySpeech(conn, query)

        print("Recognizing...")
        return query, connection