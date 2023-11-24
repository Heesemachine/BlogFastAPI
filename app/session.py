from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

engine = create_engine(
    f"mysql+pymysql://root:"
    f"@127.0.0.1:3306/blog_fastapi"
)

sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


class Base(DeclarativeBase):
    pass


# @contextmanager
def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()