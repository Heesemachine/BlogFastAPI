from pydantic import BaseModel

class Post(BaseModel):
    title: str
    description: str

class Comment(BaseModel):
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "description": "Very interesting comment"
                }
            ]
        }
    }

class LikedPost(BaseModel):
    id: int

    user_id: int
    post_id: int