from app.models.schemas import QueryRequest, QueryResponse, SourceReference
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.llm_service import LLMService


class RAGService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.llm_service = LLMService()

    def answer_question(self, request: QueryRequest) -> QueryResponse:
        query_embedding = self.embedding_service.embed_text(request.question)
        matches = self.vector_store.similarity_search(query_embedding, top_k=request.top_k)

        context = "\n\n".join(match["chunk"] for match in matches)
        answer = self.llm_service.generate_answer(request.question, context)

        sources = [
            SourceReference(
                source=match["source"],
                score=round(float(match["score"]), 4),
            )
            for match in matches
        ]

        return QueryResponse(answer=answer, sources=sources)
