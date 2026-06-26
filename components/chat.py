"""
Chat interface component: renders conversation history and handles user input.
"""

import streamlit as st
from utils.rag_chain import run_query


STARTER_QUESTIONS = [
    "What are the key trends in this data?",
    "Summarize the most important findings.",
    "Which category has the highest total value?",
    "Are there any anomalies or outliers?",
    "What actionable insights can you provide?",
]


def render_chat():
    st.markdown("### Chat with your data")

    # Starter prompts when no conversation yet
    if not st.session_state.get("messages"):
        st.markdown("**Try asking:**")
        cols = st.columns(len(STARTER_QUESTIONS))
        for i, q in enumerate(STARTER_QUESTIONS):
            if cols[i].button(q, key=f"starter_{i}", use_container_width=True):
                _handle_message(q)

    # Render history
    for msg in st.session_state.get("messages", []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander("Source references", expanded=False):
                    for src in msg["sources"]:
                        meta = src.metadata
                        label = meta.get("source", "unknown")
                        page = meta.get("page") or meta.get("row")
                        label_str = f"{label}" + (f" · row {page}" if page is not None else "")
                        st.caption(label_str)
                        st.text(src.page_content[:300] + ("..." if len(src.page_content) > 300 else ""))

    # Input box
    if prompt := st.chat_input("Ask anything about your data..."):
        _handle_message(prompt)


def _handle_message(prompt: str):
    if "chain" not in st.session_state:
        st.warning("Please upload and process at least one file first.")
        return

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = run_query(st.session_state["chain"], prompt)
            answer = result["answer"]
            sources = result["sources"]

        st.markdown(answer)

        if sources:
            with st.expander("Source references", expanded=False):
                for src in sources:
                    meta = src.metadata
                    label = meta.get("source", "unknown")
                    page = meta.get("page") or meta.get("row")
                    label_str = f"{label}" + (f" · row {page}" if page is not None else "")
                    st.caption(label_str)
                    st.text(src.page_content[:300] + ("..." if len(src.page_content) > 300 else ""))

    st.session_state["messages"].append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })
