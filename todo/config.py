import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name = os.getenv('NAME_APP')
    db_sqlite_url = os.getenv('SQLALCHEMY_DATABASE_URI')
    # db_postgre_url = os.getenv('POSTGRES_DB')

    class Config:
        env_file: str = '../.env'


settings = Settings()
