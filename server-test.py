import os
import requests

authorization_whapi = os.environ['authorization_whapi']
group_id = os.environ['group_id']
mycredential = os.environ['mycredential']
proxy_link = os.environ['proxy_link']
spreadsheet_link = os.environ['spreadsheet_link']

def send_messages(text):
    url = "https://gate.whapi.cloud/messages/text"

    payload = {
        "typing_time": 5,
        "to": str(group_id),
        "body": text
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": str(authorization_whapi)
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

send_messages("Server Test: Check")
