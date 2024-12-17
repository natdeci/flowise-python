import requests

API_URL = "http://localhost:3000/api/v1/prediction/16c6ebd3-039a-4812-a3a3-9cddfa0e0c5c"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})

print(output)