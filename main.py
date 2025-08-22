from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id:int, q: Union[str,None] = None):
    return {"item_id:": item_id, "q:":q}

@app.get("/data")
async def get_data(type: str, span: str):
    return {"data": "have fun"}