from ciscosparkapi import CiscoSparkAPI
import requests
import json
import os

#Creation of the Team
url = 'https://api.ciscospark.com/v1/teams'
payload = {'name': 'Test'}
headers = {'content-type': 'application/json; charset=utf-8',
           'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",

           }

r = requests.post(url, data=json.dumps(payload), headers=headers)

print("r.text : " + r.text)

s = json.dumps(r.text)
print("s : " + s)
#obtain_id = r.text[7:83]
obtain_id = r.json()["id"]


print("obtain_id : " + obtain_id)
#group1 = obtain_id[2:84]
#print("Id:",group1)

#Invitation of myself by the bot to the team

url1 = 'https://api.ciscospark.com/v1/team/memberships'
payload1 = {'teamId': obtain_id,'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMDI0MjljMC1mMTY0LTQ5YzMtOWU1ZS0xMGQ0YWRhNTljNWI'}
headers1 = {'content-type': 'application/json; charset=utf-8',
            'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",

           }

r1 = requests.post(url1, data=json.dumps(payload1), headers=headers1)

print("r1.text : " + r1.text)

#Team to room twosome

url2 = "https://api.ciscospark.com/v1/rooms"
payload2 = {'teamId': obtain_id,'title': 'Chamber of the secrets II'}
headers2 = {'content-type': 'application/json; charset=utf-8',
            'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",

           }


r2 = requests.post(url2, data=json.dumps(payload2), headers=headers2)

print ("r2.text : " + r2.text)
roomId = r2.json()

roomId = roomId["id"]
#    print("id " + str(x) + " :")
print json.dumps(roomId, sort_keys=True, indent=4)

print ("roomId = " + roomId)

#Message d'accueil

url3 = "https://api.ciscospark.com/v1/messages"

payload3 = {'roomId': roomId,'text': 'Welcome to the Chamber of the secrets II'}
r3 = requests.post(url3, data=json.dumps(payload3), headers=headers2)
print ("r3.text :" + r3.text)