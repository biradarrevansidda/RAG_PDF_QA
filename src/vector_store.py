from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
    COLLECTION_NAME,
    TOP_K
)


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vector_store(chunks):
    Path(VECTOR_DB_PATH).mkdir(
        parents=True,
        exist_ok=True
    )

    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=VECTOR_DB_PATH,
        collection_name=COLLECTION_NAME
    )


def get_retriever(vector_store):
    return vector_store.as_retriever(
        search_kwargs={"k": TOP_K}
    )
