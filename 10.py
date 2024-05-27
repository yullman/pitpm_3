from enum import Enum
from typing import Set, List, Union
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field



class User(str, Enum):
    Name = "test1"
    Password = "test2"
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Name": "test",
                    "Password": "test",
                }
            ]
        }
    }


user = User

app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != user.Name:
        return "Error"
    elif password != user.Password:
        return "Error"
    else:
        results = {"Name": user.Name}
        return results