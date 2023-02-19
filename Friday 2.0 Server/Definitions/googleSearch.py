from Basic import speak
from getCommands import takeMic

def googleSearch(conn):
    speak(conn, "What would you like to search for?")
    search, connection = takeMic(conn)
    search = search.lower() 
    print(search)
    speak(conn, "googleSearch "+search)


