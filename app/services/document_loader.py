import os
from app.core.config import get_settings
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.utils.text_splitter import split_text


def build_vector_index() -> None:
    settings = get_settings()
    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    os.makedirs(settings.documents_path, exist_ok=True)

    records = []

    for filename in os.listdir(settings.documents_path):
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(settings.documents_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        chunks = split_text(
            content,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )

        for index, chunk in enumerate(chunks):
            records.append(
                {
                    "id": f"{filename}-{index}",
                    "source": filename,
                    "chunk": chunk,
                    "embedding": embedding_service.embed_text(chunk),
                }
            )

    vector_store.save(records)
    print(f"Indexed {len(records)} chunks from {settings.documents_path}")


if __name__ == "__main__":
    build_vector_index()
