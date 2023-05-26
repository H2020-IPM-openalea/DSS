
from fastapi import FastAPI

from json_to_pydantic import json_to_pydantic,jsontext


json_to_pydantic(jsontext)


import pydantic_input_model

app = FastAPI()


@app.post("/items/")
async def create_item(item: pydantic_input_model.Model):
    dang=item.dict()["weatherData"]
    return [dang,"validated"]