import json
import math
import os
from typing import List, Dict, Any
from app.core.config import get_settings


class VectorStore:
    """
    Simple JSON vector store for demonstration.
    Replace with FAISS, Pinecone, Weaviate, Qdrant, Azure AI Search, or pgvector in production.
    """

    def __init__(self):
        self.settings = get_settings()
        self.index_file = os.path.join(self.settings.vectorstore_path, "index.json")
        os.makedirs(self.settings.vectorstore_path, exist_ok=True)

    def save(self, records: List[Dict[str, Any]]) -> None:
        with open(self.index_file, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=2)

    def load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.index_file):
            return []

        with open(self.index_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def similarity_search(self, query_embedding: List[float], top_k: int = 4) -> List[Dict[str, Any]]:
        records = self.load()

        for record in records:
            record["score"] = self._cosine_similarity(query_embedding, record["embedding"])

        return sorted(records, key=lambda item: item["score"], reverse=True)[:top_k]

    @staticmethod
    def _cosine_similarity(a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot / (norm_a * norm_b)
