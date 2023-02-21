from concurrent.futures import thread
from email import message
import sys
import pyjokes
import random
import socket
from _thread import *
import threading

sys.path.insert(0, './Definitions')
from Startup import *
from getCommands import *
from Basic import *
from Whatsapp import *
from googleSearch import *
from wiki import *
from Youtube import *
from weather import *
from News import *

# server constants
import json
with open('../Information/public.json') as public:
    publicData = json.load(public)

HOST = publicData["IPAddressServer"] # The server's hostname or IP address #HOST = '127.0.0.1'
PORT = publicData["Port"]  # The port used by the server
connection = True

def threaded(conn):
    connection = True
    startup(conn)

    while True:
        if (connection == False):
            break

        #Takes input
        query, connection = takeMic(conn)
        query = query.lower()        
        print(query)
        if ("friday" in query):
            speak(conn, "Now Listening")    
            while True:
                query, connection = takeMic(conn)
                query = query.lower()

                if (connection == False):
                    break

                # Date 
                closeDate = ["close", "date"]
                if all(i in query for i in closeDate):
                    speak(conn, "closeDate")
                elif 'date' in query:
                    date(conn)
                
                # Outputs the time 
                if 'time' in query:
                    time(conn)
                    
                # Can change voice from male to female 
                male = ["voice", "male"]
                female = ["voice", "female"]
                if all(i in query for i in female):
                    setVoice(conn, "female")
                elif all(i in query for i in male):
                    setVoice(conn, "male")
                    
                # Sends Whatsapp message to whoever
                Message = ["type", "message"]
                if all(i in query for i in Message):
                    typeMessage(conn)
                elif 'message' in query:
                    speakMessage(conn)

                # Search 
                if 'wikipedia' in query:
                    Wikipedia(conn)
                elif 'youtube' in query:
                    youtube(conn)
                elif 'search' in query:
                    googleSearch(conn)
                    
                # Weather
                sayWindsorWeather = ['windsor', 'weather'] 
                sayWindsorTemp = ['windsor', 'temperature'] 
                if all(i in query for i in sayWindsorWeather):
                    windsorWeather(conn)
                elif all(i in query for i in sayWindsorTemp):
                    windsorTemp(conn)
                elif 'weather' in query:
                    torontoWeather(conn)
                elif 'temperature' in query:
                    torontoTemp(conn)
                
                # News
                closeNews = ["close", "news"]
                if all(i in query for i in closeNews):
                    speak(conn, "closeNews")
                elif 'news' in query:
                    news(conn)

                tellJoke = ['real', 'joke'] 
                fakeJoke = ['another', 'joke'] 
                if all(i in query for i in tellJoke):
                    speak(conn, str(pyjokes.get_jokes()[random.randint(0,50)]))
                elif all(i in query for i in fakeJoke):
                    speak(conn, "The fact that kaleel thought he could win")
                elif 'joke' in query:
                    speak(conn, "That kaleel thought he could win")

                
                if 'read' in query:
                    speak(conn, "readText")

                openVS = ['open', 'vs']
                openVisual = ['open', 'visual']  
                openGoogle = ['open', 'google']
                openTerminal = ['open', 'terminal']
                openSolidworks = ['open', 'solidworks']
                if (all(i in query for i in openVS) or all(i in query for i in openVisual)):
                    speak(conn, "openVisual")  
                if all(i in query for i in openGoogle):
                    speak(conn, "openGoogle") 
                if all(i in query for i in openTerminal):
                    speak(conn, "openTerminal")
                if all(i in query for i in openSolidworks):
                    speak(conn, "openSolidworks")

                # Spotify
                playLikedSongs = ['play', 'spotify']
                playVibes = ['play', 'vibes']
                playVibe = ['play', 'vibe']
                playSlow = ['play', 'slow']
                playTunes = ['play', 'tunes']
                closeSpotify = ['close', 'spotify']
                if (all(i in query for i in playLikedSongs)):
                    speak(conn, "playLikedSongs")
                if (all(i in query for i in playVibes) or all(i in query for i in playVibe)):
                    speak(conn, "playVibe") 
                if (all(i in query for i in playSlow)):
                    speak(conn, "playSlow")
                if (all(i in query for i in playTunes)):
                    speak(conn, "playTunes") 
                if (all(i in query for i in closeSpotify)):
                    speak(conn, "closeSpotify") 

                #Closing windows and app
                closeMatter = ["close", "matter"]
                closeDialog = ["close", "dialog"]
                closeList = ["close", "list"]
                closeFriday = ["close", "friday"]

                if all(i in query for i in closeMatter):
                    speak(conn, "closeMatter")
                if all(i in query for i in closeDialog):
                    speak(conn, "closeDialog")
                if all(i in query for i in closeList):
                    speak(conn, "closeList")
                if all(i in query for i in closeFriday):
                    speak(conn, "closeFriday")
                    connection = False
                    break

                stopListening = ["stop", "bye", "goodnight", "mute", "go to sleep"]
                if any(i in query for i in stopListening):
                    print("Shutting down")
                    speak(conn, "Shutting down")
                    break

    conn.close()
            
                        
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Connected to: ', addr[0], ':', str(addr[1]))

        start_new_thread(threaded, (conn,))



