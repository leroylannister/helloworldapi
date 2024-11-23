from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class greetingrequest(BaseModel):
    name: str 

@app.get("/")
def helloworld():
    return "hello world"

@app.post("/")
def greet(data: greetingrequest)->str:
    """greets user with name"""
    return f"greetings {data.name}"