import json
logging = int(input())
Passwd = int(input())
data = [logging,Passwd]
def register(logging, Passwd):
    with open('1.json', 'w') as f:
         json.dump(logging, Passwd, f)
