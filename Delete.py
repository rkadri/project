from signal import pause

import requests
import json
import time


url1 = "https://api.ciscospark.com/v1/teams"

headers1 = {
    'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",
    'Content-Type': "application/json; charset=utf-8",
    'Cache-Control': "no-cache"
    }

# response1 = requests.request("GET", url1, headers=headers1)
response1 = requests.get(url1, headers=headers1)

print ("response1.text :" + response1.text)


id = response1.json()
for x in range(100):
    testID = id["items"][x]["id"]
    print("id " + str(x) + " :")
    print json.dumps(testID, sort_keys=True, indent=4)
    url2 = "https://api.ciscospark.com/v1/teams/"+testID
    print ("Deleting URL2=" + url2)
    headers2 = {
        'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",
        'Cache-Control': "no-cache",
        'Content-type':"application/json; charset=utf-8",
    }

    response = requests.request("DELETE", url2, headers=headers2)
    print(response.text)
    time.sleep(1)

# Afficher le JSON de facon elegante
print json.dumps(testID, sort_keys=True, indent=4)




