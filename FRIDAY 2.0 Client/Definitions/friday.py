from tkinter import *

def closeFriday(friday, voice):
    friday.destroy()
    voice.destroy()
    
    friday.update()
    voice.update()

    return friday, voice