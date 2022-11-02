import datetime
from Basic import speak
 
 
def greeting(conn):
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak(conn, "Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak(conn, "Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak(conn, "Good evening sir!")
    else:
        speak(conn, "For you sir, I'm always up!")
        
def startup(conn):
    greeting(conn)
    speak(conn, "Friday is now at your service")
    
    