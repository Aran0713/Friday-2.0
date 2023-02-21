import json
from Basic import *

def rentalAgreement(query, conn):
    with open('.././Information/public.json') as public:
        publicData = json.load(public)

    queryArray = query.split(" ")
    result = ""
    for i in range (len(queryArray)):
        sentence = ""
        for j in range(i, len(queryArray)):
            if i==j:
                sentence = queryArray[j]
            else:
                sentence = " ".join([sentence, queryArray[j]])

            if sentence in publicData:
                result = sentence

        if result != "":
            speak(conn, ("The "+ result+ " is " + publicData[result]))
            break