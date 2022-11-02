import clipboard
from Speak import *

def readText():
    text = clipboard.paste()
    speak(text)
    