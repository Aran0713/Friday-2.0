from tkinter import *
import pyautogui
from newsapi import NewsApiClient
import json
with open('.././Information/public.json') as public:
    publicData = json.load(public)

newsapi = NewsApiClient(api_key=publicData["newsApiKey1"]) 

width, height = pyautogui.size()

def createNewsWindow(topic):
    data = newsapi.get_everything(q= topic,language='en',page_size=5)
    newsdata = data['articles']
    
    ##### Bottom center #####
    matterWidth = str(round(0.55*width))
    matterHeight = str(round(0.53*height))
    matterXPosition = str(round(0.22*width))
    matterYPosition = str(round(0.35*height))

    
    matter = Toplevel()
    matter.title('')
    matter.geometry(matterWidth+"x"+matterHeight+"+"+matterXPosition+"+"+matterYPosition)
    matter.configure(bg="black")
    matter.attributes('-alpha',0.8)
    
    # Matter At Hand label
    TopicLabel = Label(matter, text=topic.capitalize(), bg="black", fg="white", font=("Courier 20 underline")).pack(pady=2)
    
    for x,y in enumerate(newsdata):
        titleLabel = Label(matter, text=f'{y["title"]}', bg="black", fg="white", font=("Courier 12 underline"), wraplength=600, justify="center").pack(pady=2)
        descriptionLabel = Label(matter, text=f'{y["description"]}', bg="black", fg="white", font=("Courier 12"), wraplength=1000, justify="left").pack(pady=2, padx=10, anchor="w")
        
    return matter




def closeMatter(matter):
    matter.destroy()
    matter.update()
    return matter