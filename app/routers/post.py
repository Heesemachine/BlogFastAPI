from fastapi import FastAPI, APIRouter

post_router = APIRouter(tags=['Posts'])

@post_router.get('/create')
async def create_post():
    return {"message": "Create post"}