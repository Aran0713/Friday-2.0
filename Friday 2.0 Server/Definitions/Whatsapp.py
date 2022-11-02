from time import sleep
from Basic import *
from getCommands import *

def sendWhatsappMsg(phone_no, message, conn):
    speak(conn, "Whatsapp " + 'http://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
    
username = {
    'myself': '+1 647 619 0713',
    'brother': '+1 647 482 4246',
    'dad': '+1 416 418 0037',
    'mom': '+1 647 779 8572',
    'poo': '+1 647 608 7633',
    'kish': '+1 647 332 2215',
    'meera': '+1 416 655 2240',
    'zip': '+1 416 824 0567',
    'mark': '+1 647 533 1234',
    'box': '+1 647 632 1709'
}

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
            name = takeMic(conn).lower()
            if (name == "null"): 
                speak(conn, "Would you like to try sending a message again?")
                break
            phone_no = username[name]    
            print(phone_no)
                                
            speak(conn, "What would you like to send?")
            message = takeMic(conn)
            if (message == "null"):
                speak(conn, "Would you like to try sending a message again") 
                break
                                
            sendWhatsappMsg(phone_no, message, conn)
            speak(conn, "The message to " +name+ " has been sent")
            break

        except Exception as e:
            speak(conn, "Sorry, they are not in my database")
            break