from fastapi import FastAPI, Response, status
from pydantic import BaseModel, validator
from utilities.utilities import json_parser

import uvicorn
import json

# 1. Insercion de datos de usuario y el email path="v1/insert"
# 2. Extraer mi usuario path="v1/extract"


app = FastAPI(
    title="Api testing utilities ingestion",
    version="0.1"
)


class Item(BaseModel):
    email: str
    user: str

    @validator('email', each_item=True)
    def check_len(cls, data):
        if len(data) > 40:
            raise ValueError("Es mayor que la longitud esperada")
        return data


@app.post("/v1/insert")
async def insert_data_db(item: Item, response: Response):
    email = json_parser(item, 'email')
    user = json_parser(item, 'user')

