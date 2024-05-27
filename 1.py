from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# 1
'''
@app.get("/")
async def root():
    return "Hello World"
'''

'''
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
'''

'''
@app.get("/{item_id}")
async def read_item(item_id):
    return "вы перешли по /" + item_id
'''

'''
@app.get("/{item}")
async def read_item(item: int):
    return item
'''

'''
@app.get("/{item}")
async def read_item(item: float):
    return item
'''