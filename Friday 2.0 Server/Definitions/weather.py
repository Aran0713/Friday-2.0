import requests
from Basic import *

#https://api.openweathermap.org/data/2.5/weather?lat=43.77&lon=-79.23&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b


# Toronto
def torontoWeather(conn):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.777702&lon=-79.233238&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b'
    res = requests.get(url)
    data = res.json()

    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = str(data['main']['temp'])
    temp_feels_like = str(data['main']['feels_like'])
    pressure = str(data['main']['pressure'])
    wind_speed = str(data['wind']['speed'])
    humidity = str(data['main']['humidity'])

    speak(conn, "The weather in Toronto is "+ temperature +" degrees celsius.")
    speak(conn, "With "+description+".")
    speak(conn, "The humidity is "+ humidity + ".")
    speak(conn, "And the wind speed is "+wind_speed+".")

def torontoTemp(conn):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.777702&lon=-79.233238&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b' 
    res = requests.get(url)
    data = res.json()

    temperature = str(data['main']['temp'])

    speak(conn, "The temperature in Toronto is "+ temperature +" degrees celsius")


# Windsor
def windsorWeather(conn):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=42.3149&lon=-83.0364&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b'         
    res = requests.get(url)
    data = res.json()

    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = str(data['main']['temp'])
    temp_feels_like = str(data['main']['feels_like'])
    pressure = str(data['main']['pressure'])
    wind_speed = str(data['wind']['speed'])
    humidity = str(data['main']['humidity'])

    speak(conn, "The weather in Windsor is "+ temperature +" degrees celsius.")
    speak(conn, "With a "+description+".")
    speak(conn, "The humidity is "+ humidity + ".")
    speak(conn, "And the wind speed is "+wind_speed+".")

def windsorTemp(conn):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=42.3149&lon=-83.0364&units=metric&appid=ed5b8dbb31740d7d0921491b323ed14b'    
    res = requests.get(url)
    data = res.json()

    temperature = str(data['main']['temp'])

    speak(conn, "The temperature in Windsor is "+ temperature +" degrees celsius")