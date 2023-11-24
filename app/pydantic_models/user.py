from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    nickname: str
    email: str
    password: str



