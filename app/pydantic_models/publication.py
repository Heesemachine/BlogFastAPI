from pydantic import BaseModel

class Post(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    likes: int
    comments: int

class Comment(BaseModel):
    id: int
    user_id: int
    post_id: int
    description: str

class LikedPosts(BaseModel):
    user_id: int
    post_id: int