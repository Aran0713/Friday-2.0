from logging import root
from tkinter import *
import os
from turtle import width
import pyautogui
os.system('cls')
import datetime
from Client import *
from newsapi import NewsApiClient

import json
with open('../Information/public.json') as public:
    publicData = json.load(public)

width, height = pyautogui.size()


##### Top  Center #####
fridayWidth = str(round(0.25*width))
fridayHeight = str(round(0.10*height))
fridayXPosition = str(round(width/2 - int(fridayWidth)/2))

friday = Tk()
friday.title('')
friday.geometry(fridayWidth+"x"+fridayHeight+"+"+fridayXPosition+"+20")
friday.configure(bg="black")
friday.attributes('-alpha',0.7)

friday.overrideredirect(True)
titleBar = Frame(friday, bg="black", relief="solid", bd=2)
titleBar.pack(fill=X)
titleLabel = Label(titleBar, text="", bg="black", fg="white")
titleLabel.pack(pady=4)
#titleBar.bind("<B1-Motion>", move_app)

# Friday label
#fridayLabel = Label(friday, text="F.R.I.D.A.Y", bg="black", fg="white", font=("Courier, 45"))
fridayLabel = Label(friday, text="STAN", bg="black", fg="white", font=("Courier, 45"))
fridayLabel.place(relx=0.5,rely=0.5, anchor='center')



##### Top Left corner #####
dateWidth = str(round(0.07*width))
dateHeight = str(round(0.07*width))
year = str(datetime.datetime.now().year)
day = str(datetime.datetime.now().day)
monthNum = datetime.datetime.now().month
month = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}

date = Toplevel()
date.title('')
date.geometry(dateWidth+"x"+dateHeight+"+5+5")
date.configure(bg="black")
date.attributes('-alpha',0.8)

# Month label
monthLabel = Label(date, text=month[monthNum], bg="black", fg="white", font=("Courier, 25"))
monthLabel.pack()
# Day label
dayLabel = Label(date, text=day, bg="black", fg="white", font=("Courier, 25"))
dayLabel.pack()




##### Top Right #####
voiceWidth = str(round(0.25*width))
voiceHeight = str(round(0.13*width))
voiceXPosition = str(round(width-int(voiceWidth)-20))

voice = Toplevel()
voice.title('')
voice.geometry(voiceWidth+"x"+voiceHeight+"+"+voiceXPosition+"+20")
voice.configure(bg="black")
voice.attributes('-alpha',0.8)




##### Bottom Left #####
newsapi = NewsApiClient(api_key=publicData["newsApiKey1"]) 
newsWidth = str(round(0.18*width))
newsHeight = str(round(0.55*height))
newsYPosition = str(round(0.35*height))

news = Toplevel()
news.title('')
news.geometry(newsWidth+"x"+newsHeight+"+5+"+newsYPosition)
news.configure(bg="black")
news.attributes('-alpha',0.8)

topHeadlineLabel = Label(news, text="Top Headlines", bg="black", fg="white", font=("Courier 20 underline")).pack(pady=5)

data = newsapi.get_everything(q= "science",language='en',page_size=5)
newsdata = data['articles']
scienceLabel = Label(news, text="Science", bg="black", fg="white", font=("Courier 15 underline")).pack(pady=2, anchor="w")
titleLabel = Label(news, text=newsdata[0]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[1]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[3]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[4]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
    
data = newsapi.get_everything(q= "technology",language='en',page_size=5)
newsdata = data['articles']
TechnologyLabel = Label(news, text="Technology", bg="black", fg="white", font=("Courier 15 underline")).pack(pady=2, anchor="w")
titleLabel = Label(news, text=newsdata[0]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[1]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)

titleLabel = Label(news, text=newsdata[2]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[3]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)
titleLabel = Label(news, text=newsdata[4]["title"], bg="black", fg="white", font=("Courier 10"), wraplength=300, justify="center").pack(pady=2)




##### Bottom Right #####
toDoWidth = str(round(0.18*width))
toDoHeight = str(round(0.55*height))
toDoXPosition = str(round(width-int(toDoWidth)-20))
toDoYPosition = str(round(0.35*height))

toDo = Toplevel()
toDo.title('')
toDo.geometry(toDoWidth+"x"+toDoHeight+"+"+toDoXPosition+"+"+toDoYPosition)
toDo.configure(bg="black")
toDo.attributes('-alpha',0.8)

# todo label
toDoLabel = Label(toDo, text="To Do List", bg="black", fg="white", font=("Courier 20 underline"))
toDoLabel.pack(pady=10)

for i in publicData["toDoList"]:
    listNum = Label(toDo, text="- "+ i, bg="black", fg="white", font=("Courier 10"),  wraplength=330, justify="left")
    listNum.pack(padx= 5, pady=5, anchor="w")


friday.after(2000, FridayVoiceControl(friday, voice, date, news, toDo))
friday.mainloop()
