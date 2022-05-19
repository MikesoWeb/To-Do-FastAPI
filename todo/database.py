import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from todo.config import settings


# Путь к базе данных, если нет, то создаем
BASE_DIR = os.path.dirname(os.path.abspath(__name__))

db_path = os.path.join(BASE_DIR, 'todo', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

SQLALCHEMY_DATABASE_URL = settings.db_url
#  Аргумент connect_args={"check_same_thread": False} нужен только для SQLite. Это не нужно для других баз данных
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



