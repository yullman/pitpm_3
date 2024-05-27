from enum import Enum
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

class User(str, Enum):
    description: str | None = Field(
        default=None, title="title", max_length=10
    )
    cost: float = Field(gt=0, description="description")

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
    
