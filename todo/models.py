from sqlalchemy import Column, String, Integer, Boolean

from todo.database.base import Base, choose_db, check_db


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)


Base.metadata.create_all(bind=choose_db(arg_db=check_db))
