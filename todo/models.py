from sqlalchemy import Boolean, Column, Integer, String

from todo.database import db


class ToDo(db):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)
