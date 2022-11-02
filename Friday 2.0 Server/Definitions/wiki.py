from Basic import speak
from getCommands import takeMic

def Wikipedia(conn):
    speak(conn, "What would you like to search for?")
    search = takeMic(conn)
    speak(conn, "Searching on wikipedia")
    speak(conn, "wikiSearch "+search)

    
    