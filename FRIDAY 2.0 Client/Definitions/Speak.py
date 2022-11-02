from tkinter import *
import pyttsx3 # text to speech library
import pyautogui


engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 173)  



### Speak 
def speak(audio):
    #print(audio)
    engine.say(audio)
    engine.runAndWait()
    

def setVoice(voice):
    if voice == "male":
        engine.setProperty('voice', voices[0].id)
    elif voice == "female":
        engine.setProperty('voice', voices[1].id)






def voiceWindow(voice, speech, voice1, voice2, voice3, voice4, voice5):
    width, height = pyautogui.size()
    voiceWidth = str(round(0.25*width))
    voiceHeight = str(round(0.13*width))
    voiceXPosition = str(round(width-int(voiceWidth)-20))

    voice5 = voice4
    voice4 = voice3
    voice3 = voice2
    voice2 = voice1
    voice1 = speech
    if (voice2[1] == ""):
        voice2[1] = "black"
    if (voice3[1] == ""):
        voice3[1] = "black"
    if (voice4[1] == ""):
        voice4[1] = "black"
    if (voice5[1] == ""):
        voice5[1] = "black"
        
    voice.destroy()
    
    voice = Tk()
    voice.title('')
    voice.geometry(voiceWidth+"x"+voiceHeight+"+"+voiceXPosition+"+20")
    voice.configure(bg="black")
    voice.attributes('-alpha',0.8)

    voiceLabel1 = Label(voice, text=voice1[0], bg="black", fg=voice1[1], font=("Courier, 13"), wraplength=450, justify="center").pack(pady=10)
    voiceLabel2 = Label(voice, text=voice2[0], bg="black", fg=voice2[1], font=("Courier, 13"), wraplength=450, justify="center").pack(pady=10)
    voiceLabel3 = Label(voice, text=voice3[0], bg="black", fg=voice3[1], font=("Courier, 13"), wraplength=450, justify="center").pack(pady=10)
    voiceLabel4 = Label(voice, text=voice4[0], bg="black", fg=voice4[1], font=("Courier, 13"), wraplength=450, justify="center").pack(pady=10)
    voiceLabel5 = Label(voice, text=voice5[0], bg="black", fg=voice5[1], font=("Courier, 13"), wraplength=450, justify="center").pack(pady=10)
    
    voice.update()
    
    return voice1, voice2, voice3, voice4, voice5, voice


def closeDialog(voice):
    voice.destroy()
    voice.update()
    return voice