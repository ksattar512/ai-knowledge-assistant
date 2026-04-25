from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Enterprise RAG Knowledge Assistant"
    environment: str = "development"

    openai_api_key: str = ""
    api_key: str = "local-dev-key"

    documents_path: str = "data/documents"
    vectorstore_path: str = "data/vectorstore"

    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o-mini"

    chunk_size: int = 900
    chunk_overlap: int = 120

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
