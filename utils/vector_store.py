import os
from typing import List, Optional
from pathlib import Path

from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )


def build_vector_store(docs: List[Document], persist_dir: str) -> Chroma:
    embeddings = get_embeddings()
    return Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_dir,
    )


def load_vector_store(persist_dir: str) -> Optional[Chroma]:
    if not Path(persist_dir).exists():
        return None
    try:
        return Chroma(persist_directory=persist_dir, embedding_function=get_embeddings())
    except Exception:
        return None


def add_documents_to_store(vectorstore: Chroma, docs: List[Document]) -> None:
    vectorstore.add_documents(docs)


def get_retriever(vectorstore: Chroma, k: int = 5):
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})
