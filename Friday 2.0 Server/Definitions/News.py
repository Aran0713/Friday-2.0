from newsapi import NewsApiClient
from Basic import *
from getCommands import *

def news(conn):
    newsapi = NewsApiClient(api_key='f8343e4bd0384897a38c71aec9bee17e')
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

    speak(conn, "What would you like to hear about?")
    topic, connection = takeMic(conn)
    topic = topic.lower()

    while True:
        if any(i in topic for i in categories):
            if ("business" in topic):
                speak(conn, "newsTopic " + "business")
                data = newsapi.get_everything(q= "business",language='en',page_size=5)
            elif ("entertainment" in topic):
                speak(conn, "newsTopic " + "entertainment")
                data = newsapi.get_everything(q= "entertainment",language='en',page_size=5)
            elif ("general" in topic):
                speak(conn, "newsTopic " + "general")
                data = newsapi.get_everything(q= "general",language='en',page_size=5)
            elif ("health" in topic):
                speak(conn, "newsTopic " + "health")
                data = newsapi.get_everything(q= "health",language='en',page_size=5)
            elif ("science" in topic):
                speak(conn, "newsTopic " + "science")
                data = newsapi.get_everything(q= "science",language='en',page_size=5)
            elif ("sports" in topic):
                speak(conn, "newsTopic " + "sports")
                data = newsapi.get_everything(q= "sports",language='en',page_size=5)
            elif ("technology" in topic):
                speak(conn, "newsTopic " + "technology")
                data = newsapi.get_everything(q= "technology",language='en',page_size=5)

            newsdata = data['articles']
            for x,y in enumerate(newsdata):
                speak(conn, f'{y["title"]}')
                speak(conn, f'{y["description"]}') 
        elif(topic != ''):
            print(topic)
            speak(conn, "That category is not listed")
        else:
            speak(conn, "Sorry, I couldn't hear you")
        
        speak(conn, "Would you like to hear about another topic?")
        answer, connection = takeMic(conn)
        answer = answer.lower()
        if ('yes' in answer):
            speak(conn, "closeMatter")
            topic = answer
            continue
        else:
            break
    
    speak(conn, "That's all the news for now")


