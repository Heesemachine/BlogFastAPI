from typing import Annotated

from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.pydantic_models.publication import Post, Comment
from app.models.publications import Posts, Comments, LikedPosts
from app.routers.auth import get_current_user

from app.session import get_session
from app.models.users import Users

post_router = APIRouter(prefix='/post', tags=['posts'])

db_dependency = Annotated[Session, Depends(get_session)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@post_router.get('/get_all')
def get_posts(db_session: db_dependency):
    posts = db_session.query(Posts).all()
    return posts

@post_router.get('/get_by_id')
def get_post_by_id(db_session: db_dependency, id):
    post = db_session.query(Posts).filter(Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No such post in db')
    return post


@post_router.post('/create_post')
async def create_post(db_session: db_dependency, item:Post, user: user_dependency):
    user_id = user[1]
    new_post = Posts(user_id=user_id, title=item.title, description=item.description)
    db_session.add(new_post)
    db_session.commit()
    return new_post

@post_router.put('/update_post')
async def update_post(post_id, item:Post, db_session: db_dependency, user: user_dependency):
    user_id = user[1]
    user = db_session.query(Users).filter(Users.id == user_id).first()
    post = db_session.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No such post')
    if post.user_id == user_id or user.is_admin > 0:
        post.title = item.title
        post.description = item.description
        db_session.commit()
        return post
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='You are a teapot')


@post_router.delete('/delete_post')
async def delete_post(post_id, db_session: db_dependency, user: user_dependency):
    user_id = user[1]
    user = db_session.query(Users).filter(Users.id == user_id).first()
    post = db_session.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No such post')
    if post.user_id == user_id or user.is_admin > 0:
        db_session.query(Posts).filter(Posts.id == post_id).delete()
        db_session.commit()
        return post
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='You are a teapot')


@post_router.post('/like_post')
def like_post( post_id, db_session: db_dependency, user: user_dependency):
    user_id = user[1]
    query = db_session.query(LikedPosts).filter(LikedPosts.post_id == post_id, LikedPosts.user_id == user_id)
    post = db_session.query(Posts).filter(Posts.id == post_id).first()
    if query.first():
        query.delete()
        post.likes -= 1
        db_session.commit()
        return "Unliked"

    new_like = LikedPosts(post_id=post_id, user_id=user_id)
    post.likes += 1
    db_session.add(new_like)
    db_session.commit()
    return "Liked"
