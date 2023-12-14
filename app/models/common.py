import datetime
from sqlalchemy import Column, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreateUpdateDate:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, server_default=func.now(), onupdate=func.now())

    @declared_attr
    def active(cls):
        return Column(Boolean, nullable=False, default=True, server_default="true")
