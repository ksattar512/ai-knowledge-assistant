from typing import List


def split_text(text: str, chunk_size: int = 900, chunk_overlap: int = 120) -> List[str]:
    """
    Lightweight text splitter for portfolio/demo use.
    In production, replace with semantic splitting or document-aware chunking.
    """
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks
