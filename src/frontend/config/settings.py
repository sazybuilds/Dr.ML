# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_url: str

    class Config:
        env_file: ".env"
        env_file_encoding = "utf-8"
        allow = True