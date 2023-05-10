import requests
from PIL import Image
from io import BytesIO
import base64
import os

SERV_URL = "http://localhost:5001/js/walker_run"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f"token {os.environ('JASECI_TOKEN')}"
}

def summarize(text:str) -> str:
    '''Summarizes the text using text-to-summary model'''
    payload = {
        "name": "generate_summary",
        "ctx": {
            "url": text
        }
    }
    
    response = requests.post(SERV_URL, headers=HEADERS, json=payload)
    return response.json()['report'][0][0]

def generate_image(text:str):
    '''Generates an image from the text using text-to-image model'''
    payload = {
        'name': "generate_image",
        "ctx": {
            "text": text
        }
    }
    response = requests.post(SERV_URL, headers=HEADERS, json=payload)
    generated_img = Image.open(BytesIO(base64.b64decode(response.json()['report'][0])))
    return generated_img