from typing import Union

from fastapi import FastAPI

appp = FastAPI()


@appp.get("/")
def read_root():
    return {"Hello": "World"}


@appp.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
