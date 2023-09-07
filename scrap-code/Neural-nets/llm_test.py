import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
print(API_TOKEN)

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query(
    {
        "inputs": "Django is a Python web framework known for its",
        "parameters": {"max_length": 50, "top_k": 50, "temperature": 0.7, "do_sample":False}
    }
)

print(data)
