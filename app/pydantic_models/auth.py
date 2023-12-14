from pydantic import BaseModel

class User(BaseModel):
    username: str
    nickname: str
    email: str

class UserCreating(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
