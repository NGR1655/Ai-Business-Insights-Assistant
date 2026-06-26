import os
from typing import Optional

from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma


SYSTEM_PROMPT = """You are an AI Business Insights Assistant. Analyze business data and provide actionable insights.

Use the following retrieved context to answer the question. Quote specific numbers or facts when available.
If the context does not contain relevant information, say so clearly.

Context:
{context}
"""

CONDENSE_PROMPT = PromptTemplate.from_template(
    """Given the chat history and follow-up question, rephrase it as a standalone question.

Chat history:
{chat_history}

Follow-up question: {question}
Standalone question:"""
)

QA_PROMPT = PromptTemplate(
    template=SYSTEM_PROMPT,
    input_variables=["context", "question"],
)


def build_chain(vectorstore: Chroma, memory=None):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    if memory is None:
        memory = ConversationBufferWindowMemory(
            k=6,
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
        )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        condense_question_prompt=CONDENSE_PROMPT,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT},
        return_source_documents=True,
        verbose=False,
    )
    return chain, memory


def run_query(chain, question: str) -> dict:
    result = chain.invoke({"question": question})
    return {
        "answer": result.get("answer", ""),
        "sources": result.get("source_documents", []),
    }

