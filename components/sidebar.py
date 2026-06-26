"""
Sidebar: file uploader, settings, and session controls.
"""

import os
import tempfile
import shutil
import streamlit as st
from pathlib import Path

from utils.document_processor import load_documents, split_documents, get_dataframe, SUPPORTED_EXTENSIONS
from utils.vector_store import build_vector_store, load_vector_store, add_documents_to_store
from utils.rag_chain import build_chain


def render_sidebar():
    with st.sidebar:
        st.markdown("## Settings")

        # API Key input
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            value=os.getenv("OPENAI_API_KEY", ""),
            help="Your key is used only in this session and never stored.",
        )
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

        st.divider()

        # Model selection
        model = st.selectbox(
            "Model",
            ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"],
            index=0,
        )
        os.environ["OPENAI_MODEL"] = model

        st.divider()

        # File uploader
        st.markdown("## Upload Data")
        uploaded_files = st.file_uploader(
            "CSV, Excel, PDF, or text files",
            type=["csv", "xlsx", "xls", "pdf", "txt", "md"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            if st.button("Process Files", type="primary", use_container_width=True):
                _process_files(uploaded_files)

        # Loaded files list
        if st.session_state.get("loaded_files"):
            st.divider()
            st.markdown("**Loaded files**")
            for f in st.session_state["loaded_files"]:
                st.caption(f"✓ {f}")

        st.divider()

        # Reset
        if st.button("Clear Session", use_container_width=True):
            _clear_session()
            st.rerun()

        st.markdown("---")
        st.caption("AI Business Insights Assistant")


def _process_files(uploaded_files):
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./vectorstore")
    all_docs = []
    loaded_names = []
    dataframes = {}

    progress = st.progress(0, text="Processing files...")

    for i, uf in enumerate(uploaded_files):
        progress.progress((i + 1) / len(uploaded_files), text=f"Loading {uf.name}...")

        # Save to temp file
        suffix = Path(uf.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uf.read())
            tmp_path = tmp.name

        try:
            docs = load_documents(tmp_path)
            chunks = split_documents(docs)
            all_docs.extend(chunks)

            df = get_dataframe(tmp_path)
            if df is not None:
                dataframes[uf.name] = df

            loaded_names.append(uf.name)
        except Exception as e:
            st.error(f"Error processing {uf.name}: {e}")
        finally:
            os.unlink(tmp_path)

    if all_docs:
        progress.progress(1.0, text="Building vector store...")
        existing = st.session_state.get("vectorstore")
        if existing is None:
            vs = build_vector_store(all_docs, persist_dir)
        else:
            add_documents_to_store(existing, all_docs)
            vs = existing

        chain, memory = build_chain(vs)

        st.session_state["vectorstore"] = vs
        st.session_state["chain"] = chain
        st.session_state["memory"] = memory
        st.session_state["loaded_files"] = st.session_state.get("loaded_files", []) + loaded_names
        st.session_state["dataframes"] = {**st.session_state.get("dataframes", {}), **dataframes}

        progress.empty()
        st.success(f"Loaded {len(loaded_names)} file(s). Ready to chat.")
        st.rerun()
    else:
        progress.empty()
        st.warning("No content extracted from the uploaded files.")


def _clear_session():
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./vectorstore")
    for key in ["vectorstore", "chain", "memory", "loaded_files", "dataframes", "messages"]:
        if key in st.session_state:
            del st.session_state[key]
    if Path(persist_dir).exists():
        shutil.rmtree(persist_dir, ignore_errors=True)
