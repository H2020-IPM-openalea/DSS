import json
from fastapi import FastAPI

from json_to_pydantic import json_to_pydantic,jsontext


from agroservices.ipm.ipm import IPM
import agroservices.ipm.fakers as fakers
ipm = IPM()
model = ipm.get_model(DSSId='no.nibio.vips',ModelId='PSILARTEMP')
input_data = fakers.input_data(model)

json_to_pydantic(json.dumps(input_data))


import pydantic_input_model

app = FastAPI()


@app.post("/items/")
async def create_item(item: pydantic_input_model.Model):
    dang=item.dict()["weatherData"]
    return [dang,"validated"]