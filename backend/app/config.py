from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    chroma_persist_dir: str = "./chroma_db"
    upload_dir: str = "./uploads"
    max_file_size: int = 52428800
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    llm_model: str = "HuggingFaceH4/zephyr-7b-beta"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()