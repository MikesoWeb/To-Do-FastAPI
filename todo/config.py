import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name = os.getenv("NAME_APP")
    db_url = os.getenv("SQLITE_DB")

    class Config:
        env_file: str = '../.env'


settings = Settings()


@lru_cache()
def get_settings():
    return {
        'db_url': settings.db_url,
        'app_name': settings.app_name
    }
