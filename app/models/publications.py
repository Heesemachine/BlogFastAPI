from sqlalchemy import Column, Integer, String, Text, ForeignKey
from session import Base


class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(50), nullable=True)
    description = Column(Text, nullable=False)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

class LikedPosts(Base):
    __tablename__ = 'liked_posts'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)