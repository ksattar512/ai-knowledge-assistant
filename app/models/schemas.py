from typing import List
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, description="User question")
    top_k: int = Field(default=4, ge=1, le=10, description="Number of context chunks to retrieve")


class SourceReference(BaseModel):
    source: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceReference]
