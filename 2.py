from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# 2
'''
@app.get("/users/me")
async def read_user_me():
    return {"id": "текущий пользователь"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id}
'''

'''
class Names(str, Enum):
    test1 = 'test'
    test2 = 'test2'
    
@app.get("/models/{model_name}")
async def get_model(model_name: Names):
    if model_name is Names.test1:
        return model_name +":",'сообщение 1'

    if model_name is Names.test2:
        return model_name +":",'сообщение 2'
'''

'''
class Names(str, Enum):
    test1 = 'test'
    test2 = 'test2'
    
@app.get("/models/{model_name}")
async def get_model(model_name: Names):
    if model_name is Names.test1:
        return model_name +":",'сообщение 1'

    if model_name  == 'test2':
        return model_name +":",'работает лол'
'''

'''
Names = {'test1':'сообщение1'}

    
@app.get("/models/{model_name}")
async def get_model(model_name):
    for i in Names:
        if model_name == i:
            return Names[i]
'''


'''
class ModelName(str, Enum):
    test1 = "test1"
    test2 = "test2"
    test3 = "test3"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.test1:
        return {"model_name": model_name, "message": "lol🤣"}

    if model_name.value == "test3":
        return {"model_name": model_name, "message": "lol1😊"}

    return {"model_name": model_name, "message": "lol2😂"}
'''


'''
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
'''
