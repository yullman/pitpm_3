from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class User(str, Enum):
    name = "test1"
    password = "test2"


app = FastAPI()


@app.get("/{name}/{password}")
async def get_model(name: str, password: str):
    if name != User.name:
        return "Error"
    elif password != User.password:
        return "Error"
    else:
        return "Accept"
    
