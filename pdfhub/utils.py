import requests
from .models import UploadedFile
import json

def generate_source_id(pdf_file, question):
    files = [
        ('file', ('file', open(pdf_file, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'x-api-key': 'sec_HjUHWKpFAVLBTCPNvSDoug6VMjaFuaJj'
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        print('Source ID:', response.json()['sourceId'])
        return response.json()['sourceId']
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
        return None
    
def fetch_answer_from_pdf(pdf_file, question):
    source_id = generate_source_id(pdf_file, question)
    if source_id:
        headers = {
            'x-api-key': 'sec_HjUHWKpFAVLBTCPNvSDoug6VMjaFuaJj',
            "Content-Type": "application/json",
        }

        data = {
            'sourceId': source_id,
            'messages': [
                {
                    'role': "user",
                    'content': question,
                }
            ]
        }
        print(data)

        response = requests.post(
            'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

        if response.status_code == 200:
            print('Result:', response.json()['content'])
            return response.json()['content']
        else:
            print('Status:', response.status_code)
            print('Error:', response.text)
            return None
