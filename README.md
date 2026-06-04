# AI-Powered Business Insights Assistant

Ask questions about your business data in plain English. Upload CSVs, Excel sheets,
PDFs, or text documents and get answers backed by your actual data.

## Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| LLM | OpenAI GPT-4o |
| Orchestration | LangChain |
| RAG | LangChain + ChromaDB |
| Vector DB | ChromaDB |
| Analytics | Pandas + Plotly |

## Project structure

```
ai-business-insights/
├── app.py                      Main application
├── requirements.txt
├── .env.example                Copy this to .env and fill in your key
├── components/
│   ├── sidebar.py              File uploader + settings
│   ├── chat.py                 Conversational interface
│   └── analytics_view.py      KPI cards + auto charts
├── utils/
│   ├── document_processor.py  Loads CSV, Excel, PDF, TXT
│   ├── vector_store.py         ChromaDB operations
│   ├── rag_chain.py            LangChain RAG chain
│   └── analytics.py           Pandas + Plotly helpers
└── sample_data/
    └── generate_sample.py      Generates a test CSV
```

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
copy .env.example .env       # Windows
cp .env.example .env         # Mac / Linux
```

Open `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

### 4. (Optional) Generate sample data

```bash
python sample_data/generate_sample.py
```

This creates `sample_data/sample_sales.csv` with 24 months of regional sales data.

### 5. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## How to use

1. Enter your OpenAI API key in the sidebar (or set it in `.env`).
2. Upload one or more files using the sidebar uploader.
3. Click **Process Files** — documents are embedded into ChromaDB.
4. Go to the **Chat** tab and ask questions in plain English.
5. Go to the **Analytics** tab to see KPI cards, auto-generated charts, and a custom chart builder.

## Supported file types

| Format | What gets indexed |
|--------|-------------------|
| CSV | One document per row + a statistics summary |
| Excel (.xlsx, .xls) | Same as CSV |
| PDF | Text extracted from each page |
| TXT / MD | Full text content |

## Example questions

- "What was the total revenue for the North region?"
- "Which product had the highest profit margin?"
- "Summarize the key findings from the uploaded report."
- "Are there any months where costs exceeded 60% of revenue?"
- "What is the trend in customer satisfaction scores?"

## Notes

- The vector store is saved to `./vectorstore/` by default.
- Click **Clear Session** in the sidebar to delete the vector store and start over.
- For large files (thousands of rows), processing may take 30-60 seconds.
- Each API call uses your OpenAI credits. GPT-4o-mini is a cheaper alternative.
