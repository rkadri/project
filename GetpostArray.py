import requests

url1 = "https://api.ciscospark.com/v1/people?email=rkadri@cisco.com"



headers1 = {
    'Email': "rkadri@cisco.com",
    'Authorization': "Bearer MTliOGM0MTAtZjkyZi00MzY1LThhZjItYzczMDZhZGYwN2Y2NTI3ODRlZTUtNjVh",
    'Cache-Control': "no-cache",
    'Postman-Token': "e4ab4417-eb34-1441-2883-acb8280e59bb"
    }

response = requests.request("GET", url1, headers=headers1)
print(response.text)


url2 = "https://api.ciscospark.com/v1/teams"

headers2 = {
    'name': "Team Ryanator 2"
    'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",
    'Cache-Control': "no-cache",
    'Postman-Token': "e4ab4417-eb34-1441-2883-acb8280e59bb"
    }

response2 = requests.request("POST", url2, headers=headers2)
print(response2.text)