import hashlib
from typing import List


class EmbeddingService:
    """
    Embedding abstraction.

    For enterprise deployment, replace the fallback embedding with:
    - OpenAI embeddings
    - Azure OpenAI embeddings
    - AWS Bedrock embeddings
    - Local embedding models
    """

    def embed_text(self, text: str) -> List[float]:
        """
        Deterministic lightweight pseudo-embedding for local demo execution.
        This keeps the repo runnable without paid API calls.
        """
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        return [value / 255 for value in digest[:32]]
