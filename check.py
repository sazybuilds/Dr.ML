#simple python script to test settings configuration is successful
from src.training.config.settings import  Settings

settings = Settings()


log_path = settings.log_path
diabetes_data = settings.diabetes_dataset_path
print(log_path)
print(diabetes_data)