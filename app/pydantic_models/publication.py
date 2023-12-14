from pydantic import BaseModel

class Post(BaseModel):
    title: str
    description: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Some title",
                    "description": "Some description"
                }
            ]
        }
    }

class Comment(BaseModel):
    id: int
    user_id: int
    post_id: int
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