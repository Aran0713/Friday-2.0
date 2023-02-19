import pywhatkit
from Basic import speak
from getCommands import takeMic

def youtube(conn):
    speak(conn, "What would you like to search for on youtube?")
    topic, connection = takeMic(conn)
    speak(conn, "playYoutube "+ topic)
    #pywhatkit.playonyt(topic)