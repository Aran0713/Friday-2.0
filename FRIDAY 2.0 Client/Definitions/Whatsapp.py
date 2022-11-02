from time import sleep
import pyautogui
import webbrowser as web

def sendWhatsappMsg(data):
    web.open(data)
    sleep(10)
    pyautogui.press('enter')
    sleep(5)
    
