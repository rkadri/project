import requests
import json

url = "https://api.ciscospark.com/v1/team"


payload = {
    'name': "Batallion"
    }
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content': "application/json; charset=utf-8",
    'Authorization': "Bearer OTA1OTRjNTAtODI5Yi00Yjk5LTk4OGYtZTk4ODZmM2EwOTEzNzhiYTk5MGMtNzc1",
    'Cache-Control': "no-cache",
    'Postman-Token': "9adaf166-91a5-74d2-cf5d-f50a21a4ecaa"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
