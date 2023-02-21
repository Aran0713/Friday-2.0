from time import sleep
from Basic import *
from getCommands import *

# Users is a list of my conatcts which is stored in my private.json folder
import json
with open('.././Information/private.json') as private:
    privateData = json.load(private)
username = privateData["username"]

# Note: to use this function you must first connect your computer to your whatsapp

def sendWhatsappMsg(phone_no, message, conn):
    speak(conn, "Whatsapp " + 'http://web.whatsapp.com/send?phone='+phone_no+'&text='+message)

def typeMessage(conn):
    while True:
        try: 
            speak(conn, "To whom do you want to send a message to?")
            speak(conn, "typeInput "+ "Name: ")

            name = str(conn.recv(1024)).lower()
            name = name[2:len(name)-1]

            if (name == ""): 
                speak(conn, "Would you like to try sending a message again?")
                break
            phone_no = username[name]  
                                
            speak(conn, "What would you like to send?")
            speak(conn, "typeInput "+ "Message: ")
            message = str(conn.recv(1024))
            message = message[2:len(message)-1]

            if (message == ""):
                speak(conn, "Would you like to try sending a message again") 
                break
                                
            sendWhatsappMsg(phone_no, message, conn)
            speak(conn, "The message to " +name+ " has been sent")
            break
        except Exception as e:
            speak(conn, "Sorry, they are not in my database")
            break


def speakMessage(conn):
    while True:
        try:
            speak(conn, "To whom do you want to send a message to?")
            name, connection = takeMic(conn)
            name = name.lower()
            if (name == ""): 
                speak(conn, "Would you like to try sending a message again?")
                break
            for key in username:
                if(key in name):
                    name = key
                    phone_no = username[name]    
                    print(phone_no)
                                
            speak(conn, "What would you like to send?")
            message, connection = takeMic(conn)
            if (message == ""):
                speak(conn, "Would you like to try sending a message again") 
                break
                                
            sendWhatsappMsg(phone_no, message, conn)
            speak(conn, "The message to " +name+ " has been sent")
            break

        except Exception as e:
            speak(conn, "Sorry, they are not in my database")
            break