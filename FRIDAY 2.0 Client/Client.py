import socket
import sys

sys.path.insert(0, './Definitions')
from Speak import *
from Youtube import *
from google import *
from Whatsapp import *
from wiki import *
from Speak import *
from NewsWindow import *
from news import *
from toDo import *
from date import *
from friday import *
from read import *
from openPrograms import *
from spotify import *

HOST ="192.168.3.116" # The server's hostname or IP address
PORT = 65432  # The port used by the server


def FridayVoiceControl(friday, voice, date, news, toDo):
    voice1 = voice2 = voice3 = voice4 = voice5 = ["", ""]
    print("Waiting for server")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connection secured")

        check = (s.recv(1024)).decode('utf-16')
        check = str(check)
        speech = [check, "white"]
        voice1, voice2, voice3, voice4, voice5, voice = voiceWindow(voice, speech, voice1, voice2, voice3, voice4, voice5)
        
        speak(check)
        s.send(bytes("Friday has been connected", encoding='utf-8'))
                                                               

        while True: 
            data = (s.recv(1024)).decode('utf-16')
            data = str(data)
            
            # Prints my text
            if (data[0:8] == 'mySpeech'):
                data = (data[9:len(data)]).capitalize()
                speech = [data, "#ADD8E6"]
                voice1, voice2, voice3, voice4, voice5, voice = voiceWindow(voice, speech, voice1, voice2, voice3, voice4, voice5)
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            # Google Search
            if (data[0:12] == 'googleSearch'):
                googleSearch(data[13:len(data)])
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            # Changes voice to male or female
            if 'voice to male' in data:
                setVoice("male")
            elif 'voice to female' in data:
                setVoice("female")
            
            # sends Whatsapp message
            if (data[0:8] == 'Whatsapp'):
                sendWhatsappMsg(data[9:len(data)])
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            # Search on wikipedia
            if (data[0:10] == 'wikiSearch'):
                Wikipedia(data[11:len(data)])
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            # Plays on Youtube 
            if (data[0:11] == 'playYoutube'):
                youtube(data[12:len(data)])
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            if (data[0:9] == 'typeInput'):
                data = data[10:len(data)]
                msg = input(data+"\n")
                s.send(bytes("Received", encoding='utf-8'))
                s.send(bytes(msg, encoding='utf-8'))
                continue
            
            if (data[0:9] == 'newsTopic'):
                data = data[10:len(data)]
                matter = createNewsWindow(data)
                s.send(bytes("Received", encoding='utf-8'))
                continue 
            elif (data[0:len(data)] == 'closeMatter'):
                matter = closeMatter(matter)
                s.send(bytes("Received", encoding='utf-8'))
                continue 
            
            # Reads text in clipboard
            if (data[0:8] == 'readText'):
                readText()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            ### Open Programs ###
            # Opens vs code
            if (data[0:10] == 'openVisual'):
                openVS()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            # Opens Google
            if (data[0:10] == 'openGoogle'):
                openGoogle()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            # Opens Terminal
            if (data[0:12] == 'openTerminal'):
                openTerminal()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            # Opens SolidWorks
            if (data[0:14] == 'openSolidworks'):
                openSolidWorks()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            ### Spotify ###
            if (data[0:14] == 'playLikedSongs'):
                driver = playLikedSongs()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            if (data[0:8] == 'playVibe'):
                driver = vibe()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            if (data[0:8] == 'playSlow'):
                driver = slowSongs()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            if (data[0:9] == 'playTunes'):
                driver = tunes()
                s.send(bytes("Received", encoding='utf-8'))
                continue
            if (data[0:12] == 'closeSpotify'):
                closeDriver(driver)
                s.send(bytes("Received", encoding='utf-8'))
                continue
            
            
            ### Close windows ###
            if (data[0:len(data)] == 'closeDialog'):
                voice = closeDialog(voice)
                s.send(bytes("Received", encoding='utf-8'))
                continue 
            if (data[0:len(data)] == 'closeNews'):
                news = closeNews(news)
                s.send(bytes("Received", encoding='utf-8'))
                continue
            if (data[0:len(data)] == 'closeList'):
                toDo = closeList(toDo)
                s.send(bytes("Received", encoding='utf-8'))
                continue  
            if (data[0:len(data)] == 'closeDate'):
                date = closeDate(date)
                s.send(bytes("Received", encoding='utf-8'))
                continue  
            if (data[0:len(data)] == 'closeFriday'):
                s.send(bytes("Received", encoding='utf-8'))
                friday, voice = closeFriday(friday, voice)
                s.close()
                continue  
            
            # Friday voice 
            speech = [data, "white"]
            voice1, voice2, voice3, voice4, voice5, voice = voiceWindow(voice, speech, voice1, voice2, voice3, voice4, voice5)
            speak(data)
            s.send(bytes("Completed", encoding='utf-8'))
            
            
            friday.update()
            
            


    













        