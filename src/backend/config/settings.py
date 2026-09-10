# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    log_path: str
    diabetes_model_path: str
    heart_disease_model_path: str

    class Config:
        env_file=".env"
        env_file_encoding="utf-8"
        extra="allow" #allow the existence of other variables not in the settings class