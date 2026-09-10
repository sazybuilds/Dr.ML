# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #environment variables type check, ensure presence of all required environment variables
    
    log_path: str

    diabetes_dataset_path: str
    heart_disease_dataset_path: str

    diabetes_model_path: str
    heart_disease_model_path: str

    diabetes_target_col: str
    heart_disease_target_col: str

    test_size: float
    random_state: int
    hyper_params_yaml_path: str

    #failsafe in case of missing variables, we can access the .env file
    class Config:
        env_file = ".env"
        env_file_encoding= "utf-8"
        extra= "allow"

