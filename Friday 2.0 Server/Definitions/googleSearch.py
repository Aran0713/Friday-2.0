from Basic import speak
from getCommands import takeMic

def googleSearch(conn):
    speak(conn, "What would you like to search for?")
    search = takeMic(conn)
    speak(conn, "googleSearch "+search)


