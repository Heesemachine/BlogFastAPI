from fastapi import FastAPI, APIRouter

user_router = APIRouter(tags=['User'])

@user_router.get('/create')
async def create_user():
    return {"message": "Hello User"}