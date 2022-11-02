import datetime
import threading

print_lock = threading.Lock()

### Speak 
def speak(conn, audio):
    conn.send(bytes(audio, encoding='utf-16'))
    recData = conn.recv(1024)

def mySpeech(conn, audio):
    conn.send(bytes("mySpeech "+audio, encoding='utf-16'))
    recData = conn.recv(1024)
    recData = str(recData.decode('utf-8'))
    print(f"{recData!r}")
    if (recData == '') or (not recData):
        print("A")
        return False
    return True
    

    
### To change voices (male, female) 
def setVoice(conn, voice):    
    if voice == "male":
        speak(conn, "You have now switched the voice to male")
    elif voice == "female":
        speak(conn, "You have now switched the voice to female")
    

### To get the date (Month/Day/Year)
def date(conn):
    year = str(datetime.datetime.now().year)
    monthNum = datetime.datetime.now().month
    day = str(datetime.datetime.now().day)
    
    month = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    speak(conn, "The current date is " + month[monthNum] +" "+ day +", "+ year)
    
### To get the time (Hour/Min/Sec)
def time(conn):
    Time = datetime.datetime.now().strftime("%I:%M:%S") #hours:mins:secs
    speak(conn, "The current time is "+ Time)
    
