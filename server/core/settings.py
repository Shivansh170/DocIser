from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str
    SECRET_KEY:str
    
    model_config={
        "env_file":".env",
        "env_file_encoding":"utf-8",
        "extra":"ignore"
    }

settings=Settings()