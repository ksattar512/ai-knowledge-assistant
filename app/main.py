from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="Enterprise RAG Knowledge Assistant",
    description="Production-style RAG API for enterprise knowledge retrieval.",
    version="1.0.0",
)

app.include_router(router, prefix="/api", tags=["rag"])


@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "Enterprise RAG Knowledge Assistant",
        "version": "1.0.0",
    }
