# app/core/config.py
from functools import lru_cache
from pydantic import BaseModel


class Settings(BaseModel):
    app_title: str = "Clean Architecture"


@lru_cache
def get_settings() -> Settings:
    return Settings()