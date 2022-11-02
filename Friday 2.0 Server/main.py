from email import message
import sys
import socket

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
#HOST = '127.0.0.1'
HOST = '0.0.0.0'
PORT = 65432

if __name__ == "__main__":
    wakeWord = "friday"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            startup(conn)

            while True:

                #Takes input
                query = takeMic(conn).lower()
                if (wakeWord in query):
                    speak(conn, "Now Listening")                    
                    while True:
                       
                        query = takeMic(conn).lower()
                        # Output the date today
                        if 'date' in query:
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
                        if 'weather' in query:
                            weather(conn)
                        elif 'temperature' in query:
                            temp(conn)
                        
                        if 'news' in query:
                            news(conn)
                        
                        # Closes Friday/ the whole app
                        closeApp = ["close", "stop", "bye", "goodnight", "mute", "go to sleep"]
                        if any(i in query for i in closeApp):
                            print("Shutting down")
                            speak(conn, "Shutting down")
                            break
                        
                        

