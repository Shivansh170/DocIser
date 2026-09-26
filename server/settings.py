from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY:str
    DATABASE_URL:str
    
    model_config={
        "env_file":".env",
        "env_file_encoding":"utf-8",
        "extra":"ignore"
    }

settings=Settings()