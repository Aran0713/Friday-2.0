import json

with open('./Information/public.json') as public:
    publicData = json.load(public)
    
print(publicData["toDoList"])