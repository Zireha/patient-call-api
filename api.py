from fastapi import FastAPI
from call_queue import call_patient
import os
from azure.storage.blob import BlobServiceClient as BSC

app = FastAPI()

@app.get('/')
def hello():
    return{'message' : 'success',
           'response status' : '200'
           }

@app.get('/queue/call')
def get_call_voice(first_name:str, second_name:str, queue:str, room:str):
    call_patient(first_name=first_name, second_name=second_name, queue_number=queue, room=room)
    file_queue = queue + ".wav"
    path = os.path.join("..\PatientCall\\voices\\", file_queue)
    return {"path": path}

@app.get('/hello')
def hello():
    return {'message' : 'Hello!'}