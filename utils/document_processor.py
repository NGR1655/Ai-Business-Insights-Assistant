"""
Document processor: loads CSV, Excel, PDF, and plain text files.
Returns LangChain Document objects ready for embedding.
"""

import os
import pandas as pd
from pathlib import Path
from typing import List

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls", ".pdf", ".txt", ".md"}


def load_documents(file_path: str) -> List[Document]:
    ext = Path(file_path).suffix.lower()
    if ext in (".csv", ".xlsx", ".xls"):
        return _load_tabular(file_path)
    elif ext == ".pdf":
        return _load_pdf(file_path)
    elif ext in (".txt", ".md"):
        return _load_text(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def _load_tabular(file_path: str) -> List[Document]:
    ext = Path(file_path).suffix.lower()
    df = pd.read_csv(file_path) if ext == ".csv" else pd.read_excel(file_path)
    df = df.fillna("N/A")

    docs = []
    # One document per row, plus a summary document
    for idx, row in df.iterrows():
        content = "\n".join([f"{col}: {val}" for col, val in row.items()])
        docs.append(Document(
            page_content=content,
            metadata={
                "source": file_path,
                "row": idx,
                "file_type": "tabular",
                "columns": ", ".join(df.columns.tolist()),
            }
        ))

    # Summary document: column names + stats
    summary_lines = [f"Dataset: {Path(file_path).name}"]
    summary_lines.append(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    summary_lines.append(f"Columns: {', '.join(df.columns.tolist())}")
    for col in df.select_dtypes(include="number").columns:
        s = df[col]
        summary_lines.append(
            f"{col} — min: {s.min():.2f}, max: {s.max():.2f}, "
            f"mean: {s.mean():.2f}, sum: {s.sum():.2f}"
        )
    docs.insert(0, Document(
        page_content="\n".join(summary_lines),
        metadata={"source": file_path, "row": -1, "file_type": "tabular_summary"}
    ))
    return docs


def _load_pdf(file_path: str) -> List[Document]:
    from pypdf import PdfReader
    reader = PdfReader(file_path)
    docs = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if text.strip():
            docs.append(Document(
                page_content=text,
                metadata={"source": file_path, "page": i + 1, "file_type": "pdf"}
            ))
    return docs


def _load_text(file_path: str) -> List[Document]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return [Document(
        page_content=content,
        metadata={"source": file_path, "file_type": "text"}
    )]


def split_documents(docs: List[Document], chunk_size: int = 1000, chunk_overlap: int = 150) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_documents(docs)


def get_dataframe(file_path: str) -> pd.DataFrame | None:
    """Return a DataFrame for tabular files, None otherwise."""
    ext = Path(file_path).suffix.lower()
    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext in (".xlsx", ".xls"):
        return pd.read_excel(file_path)
    return None
