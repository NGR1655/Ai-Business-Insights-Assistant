"""
AI-Powered Business Insights Assistant
Entry point: run with `streamlit run app.py`
"""

import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

from components.sidebar import render_sidebar
from components.chat import render_chat
from components.analytics_view import render_analytics


st.set_page_config(
    page_title="Business Insights Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Minimal CSS: tighten up spacing and style the metric cards
st.markdown("""
<style>
[data-testid="stMetric"] {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 10px;
    padding: 14px 18px;
}
[data-testid="stChatMessage"] {
    padding: 6px 0;
}
</style>
""", unsafe_allow_html=True)


def main():
    render_sidebar()

    st.title("Business Insights Assistant")
    st.caption("Upload business data → ask questions → get insights backed by your documents.")

    # Warn if no API key
    if not os.getenv("OPENAI_API_KEY"):
        st.warning("Enter your OpenAI API key in the sidebar to get started.")

    # Main tabs
    tab_chat, tab_analytics = st.tabs(["Chat", "Analytics"])

    with tab_chat:
        render_chat()

    with tab_analytics:
        render_analytics()


if __name__ == "__main__":
    main()
