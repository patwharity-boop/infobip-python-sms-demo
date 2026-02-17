import os
import requests
from dotenv import load_dotenv

# 1. Load secrets from the .env file
load_dotenv()

BASE_URL = f"https://{os.getenv('INFOBIP_BASE_URL')}"
API_KEY = os.getenv('INFOBIP_API_KEY')
RECIPIENT_NUMBER = "15857541125"

# 2. The JSON Payload
# This is the 'Body' of the request containing the sender, receiver, and text
# 2. The JSON Payload
payload = {
    "messages": [
        {
            "from": "ServiceSMS",
            "destinations": [
                {"to": "15857541125"}
            ],
            "content": {
                "text": "Success! My first Infobip API call via Python is working."
            }
        }
    ]
}


# 3. The Headers
# This tells the server who we are (Authorization) and what format we're sending (JSON)
headers = {
    "Authorization": f"App {API_KEY}",
    "Content-Type": "application/json"
}

# 4. The Request
# We 'POST' the data to the SMS endpoint
response = requests.post(f"{BASE_URL}/sms/3/messages", json=payload, headers=headers)

# 5. Output the result to the terminal
print(f"Status Code: {response.status_code}")
print(response.json())