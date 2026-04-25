from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import QueryRequest, QueryResponse
from app.security.auth import validate_api_key
from app.services.rag_service import RAGService

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_knowledge_base(
    request: QueryRequest,
    _: bool = Depends(validate_api_key),
):
    """
    Query the enterprise knowledge base using RAG.
    """
    try:
        rag_service = RAGService()
        return rag_service.answer_question(request)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
