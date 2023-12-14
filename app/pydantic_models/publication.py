from pydantic import BaseModel

class Post(BaseModel):
    title: str
    description: str

class Comment(BaseModel):
    description: str

class LikedPost(BaseModel):
    id: int

    user_id: int
    post_id: int