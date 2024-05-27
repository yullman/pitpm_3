from enum import Enum

from fastapi import FastAPI


class User(str, Enum):
    name = "test1"
    password = "test2"


app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != User.name:
        return "Error"
    elif password != User.password:
        return "Error"
    else:
        return "Accept"
    
