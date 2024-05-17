import requests
import json
import time
import random
import pusher

pusher_client = pusher.Pusher(
  app_id='1803808',
  key='150195cef7da32949a7b',
  secret='e806343d86e5394eac73',
  cluster='ap1',
  ssl=True
)

# Define the URL of your Laravel API endpoint
url = "http://127.0.0.1:8000/api/receive-message"

# Create the message payload



# Set the headers
headers = {
    "Content-Type": "application/json"
}

while True:
    # Send the POST request
    eggs=[
        "peewee",
        "pullet",
        "small",
        "medium",
        "large",
        "extra_large",
        "jumbo",
        "crack"
    ]
    message = {
        "message": eggs[random.randrange(0,7)]
    }
    response = requests.post(url, data=json.dumps(message), headers=headers)

    # Print the response
    print(f"Message: {message}")
    print(f"Status Code: {response.status_code}")
    # print(f"Response: {response.json()}")

    time.sleep(3)