import datetime
import threading

print_lock = threading.Lock()

### Speak 
def speak(conn, audio):
    #print(conn)
    conn.send(bytes(audio, encoding='utf-16'))
    recData = conn.recv(1024)

def mySpeech(conn, audio):
    conn.send(bytes("mySpeech "+audio, encoding='utf-16'))
    recData = conn.recv(1024)
    recData = str(recData.decode('utf-8'))
    print(f"{recData!r}")
    if (recData == '') or (not recData):
        print("Not Connected")
        return False
    return conn
    

    
### To change voices (male, female) 
def setVoice(conn, voice):    
    if voice == "male":
        speak(conn, "You have now switched the voice to male")
    elif voice == "female":
        speak(conn, "You have now switched the voice to female")
    

### To get the date (Month/Day/Year)
def date(conn):
    import json 
    with open('.././Information/public.json') as public:
        publicData = json.load(public)

    year = str(datetime.datetime.now().year)
    monthNum = datetime.datetime.now().month
    day = str(datetime.datetime.now().day)

    speak(conn, "The current date is " + publicData["month"][str(monthNum)]  +" "+ day +", "+ year)
    
### To get the time (Hour/Min/Sec)
def time(conn):
    Time = datetime.datetime.now().strftime("%I:%M:%S") #hours:mins:secs
    speak(conn, "The current time is "+ Time)
    
