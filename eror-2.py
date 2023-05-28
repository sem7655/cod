import json

logging = input()
Passwd = input()
data = [logging, Passwd]

def register(logging, Passwd):
    with open('1.json', 'w') as f:
        json.dump(data, f)

register(logging, Passwd)
