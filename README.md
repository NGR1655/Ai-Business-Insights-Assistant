# 📊 AI Business Insights Assistant

<div align="center">

![Built with AI](https://img.shields.io/badge/Built%20with-Generative%20AI-0A5C47?style=for-the-badge)
![Groq LLM](https://img.shields.io/badge/LLM-Groq%20Llama%203.3%2070B-F55036?style=for-the-badge)
![Analytics](https://img.shields.io/badge/Analytics-Pandas%20%2B%20Plotly-185FA5?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-Streamlit-FF4B4B?style=for-the-badge)
![Cost](https://img.shields.io/badge/API%20Cost-%240-27AE60?style=for-the-badge)

<br/>

## *"Stop waiting for reports. Just ask."*

<br/>

A Generative AI application that turns any business file into an intelligent analyst —
answering questions, surfacing trends, and generating dashboards in seconds.

**No SQL. No formulas. No waiting for the data team.**

</div>

---

## 🧩 The Problem This Solves

Every business analyst knows this situation:

> A stakeholder walks in and asks — *"Which product line is dragging our margins down?"*
>
> You spend 2 hours pulling data, writing queries, building a chart, and formatting a slide.
>
> By the time you answer, the meeting is over.

This tool answers that question in **10 seconds**.

Upload the sales file. Type the question. Get the answer — with the exact data rows it used to reach that conclusion.

---

## 💡 What This Tool Does

<div align="center">

| Upload | Ask | Explore |
|:---:|:---:|:---:|
| Drop any business file into the app | Type your question in plain English | Browse auto-generated dashboards |
| CSV · Excel · PDF · Text | Conversational, multi-turn Q&A | KPIs · Charts · Heatmaps · Custom views |
| Processed instantly by AI | Answers grounded in your actual data | No setup, no formulas, no waiting |

</div>

---

## 🗣️ Real Conversations with Your Data

Here is what using this tool actually looks like:

```
You:   "What was our best performing region last quarter?"

AI:    "The North region generated the highest revenue at ₹18.4M,
        outperforming the company average by 23.6%.
        It also had the strongest profit margin at 47.2%."

You:   "What drove that performance?"

AI:    "The Analytics Suite product line accounted for 61% of
        North region revenue, with above-average customer
        satisfaction scores of 4.7/5.0 across that period."

You:   "Which region should we focus on to close the gap?"

AI:    "The West region shows the largest gap — revenue of ₹11.2M
        against a target of ₹15M, with cost ratios 8% above average.
        The Data Vault product line is underperforming there specifically."
```

Every answer comes with **source references** — the exact rows or pages the AI used. Nothing is invented.

---

## 📂 Works With Every Business File Format

| File Type | Business Examples | What the AI Can Do |
|---|---|---|
| **CSV** | Sales data, CRM exports, survey results, web analytics | Trend analysis, segmentation, KPI extraction, anomaly detection |
| **Excel** | Financial models, budget trackers, performance scorecards | Cross-sheet insights, variance analysis, target vs actual |
| **PDF** | Annual reports, strategy documents, market research, board packs | Key finding extraction, competitive insights, executive summary |
| **Text** | Meeting notes, requirements docs, customer feedback, emails | Theme extraction, action item identification, sentiment summary |

Upload multiple files together — the AI searches across all of them simultaneously.

---

## 📈 Instant Analytics Dashboard

Every uploaded spreadsheet or CSV automatically generates a full analytics view:

**KPI Cards**
> Total Revenue · Average Order Value · Min · Max — calculated instantly for every numeric column

**Auto-Generated Charts**
> Bar charts by category · Trend lines over time · Distribution histograms · Scatter comparisons

**Correlation Heatmap**
> See which business variables move together — identify leading indicators instantly

**Custom Chart Builder**
> Pick any two columns. Pick a chart type. Done. No pivot tables. No chart wizards.

---

## 💼 Designed for Business Roles

### For Data Analysts

This tool handles the **first 30 minutes of every analysis** — the repetitive part where you just need to understand what the data says before building the real deliverable.

| What takes hours today | What this tool does in seconds |
|---|---|
| Loading and profiling a new dataset | Auto-generates KPIs and charts on upload |
| Answering ad-hoc stakeholder questions | Conversational Q&A with source references |
| Summarising a PDF report before analysis | Ask "what are the key findings?" and get a structured answer |
| Comparing performance across segments | Ask in plain English across multiple files |
| Exploring correlations | Auto-generated heatmap with every dataset |

**This is not a replacement for a Data Analyst.** It is what a Data Analyst looks like when they use AI to deliver insights 10× faster.

---

### For Business Analysts

Business Analysts spend a disproportionate amount of time translating between data and decisions. This tool closes that gap.

| BA Workflow | How this tool helps |
|---|---|
| Stakeholder interviews and research | Upload interview notes, ask "what themes appear most?" |
| Requirements from existing documentation | Upload policy PDFs, ask "what constraints apply to X?" |
| Gap analysis across datasets | Upload current vs target data, ask "where are the biggest gaps?" |
| Presenting findings to leadership | Get precise numbers in seconds, not hours |
| Market and competitor research | Upload research PDFs, extract key insights conversationally |

A Business Analyst using this tool walks into every meeting already knowing the answer — instead of building the answer after the meeting.

---

### For Product Analysts

| Product Question | What you upload | What you ask |
|---|---|---|
| Which feature drives retention? | Usage CSV | "Which features correlate with 90-day retention?" |
| Did our A/B test work? | Results CSV | "Which variant had better conversion and why?" |
| Where do users drop off? | Funnel CSV | "At which step does engagement fall below 50%?" |
| Are users satisfied? | NPS CSV | "What is the trend in NPS over the last 6 months?" |

---

## 🔒 Your Data Stays Private

- **Files never leave your machine** — everything is processed locally
- Only your typed question is sent to the AI — never your file contents
- All analysis data is stored locally and deleted with one click
- No cloud storage. No data sharing. No subscription required.

---

## 🏗️ How the AI Works (Business Summary)

You do not need to understand this to use the tool — but here is what happens behind the scenes:

**1. Intelligent document processing**
When you upload a file, the AI breaks it into thousands of small, searchable knowledge pieces — each one representing a specific part of your data.

**2. Meaning-based search**
When you ask a question, the AI does not search for keywords. It understands the *meaning* of your question and finds the data pieces that are most relevant — even if they use different words.

**3. Grounded answer generation**
The AI reads only the most relevant pieces of your data, then generates a precise answer. It is instructed to cite its sources and say clearly if the data does not contain the answer — it will never invent numbers.

**4. Conversational memory**
The AI remembers the last 6 turns of your conversation, so follow-up questions like "What about last year?" or "Which product specifically?" work naturally.

---

## 🛠️ Technology Behind It

| Layer | Technology | Why it was chosen |
|---|---|---|
| AI Language Model | Groq — Llama 3.3 70B | Free, fast, enterprise-quality answers |
| Intelligent Search | ChromaDB + HuggingFace Embeddings | Meaning-based search, runs fully offline |
| AI Orchestration | LangChain | Connects search, memory, and LLM together |
| Analytics Engine | Pandas + Plotly | Industry-standard data analysis and visualisation |
| Interface | Streamlit | Clean, fast, business-focused web UI |
| File Processing | PyPDF + OpenPyXL | Handles PDF and Excel natively |

**Running cost: $0** — The AI model (Groq) is free. The search engine runs locally. No subscriptions.

---

## ⚙️ Get Started in 5 Minutes

**What you need:**
- Python 3.11.9
- A free Groq API key from [console.groq.com](https://console.groq.com/keys) — takes 2 minutes

**Setup:**
```bash
git clone https://github.com/NGR1655/ai-business-insights.git
cd ai-business-insights
```

Full setup instructions in [SETUP.md](SETUP.md)

Once running, open `http://localhost:8501` and upload any CSV, Excel, PDF, or text file to get started immediately.

---

## 💬 Questions to Try First

Once you have uploaded a dataset, start with these:

```
"Give me a summary of this data in 5 bullet points."
"What are the 3 most important trends I should know about?"
"Which segment is underperforming and why?"
"What is the relationship between cost and revenue?"
"If I had to focus on one area to improve performance, what would it be?"
"What does this data say about customer behaviour?"
```

---

## 📌 What Makes This Different

| Traditional Approach | This Tool |
|---|---|
| Open Excel → write pivot table → build chart → format → present | Upload → ask → done |
| Hire analyst to read 50-page report | Upload PDF → ask "key findings?" |
| Wait 2 days for data team to answer a question | Type the question, get the answer now |
| ChatGPT with file upload — data sent to OpenAI servers | Everything stays on your machine |
| Tableau / Power BI — requires pre-built dashboards | Auto-generates insights from any new file |

---

## 🛣️ What Is Coming Next

- [ ] One-click export of AI insights to a formatted PDF report
- [ ] Export filtered analytics view directly to Excel
- [ ] Public deployment so teams can use it without local setup
- [ ] Scheduled analysis — automatically analyse new data files as they arrive
- [ ] Answer quality scoring — measure how accurate the AI's answers are

---

## 👤 Built By

**Greeshma Reddy** — Data Analyst with Generative AI focus
📍 Hyderabad, India

Targeting roles in Data Analytics, Business Analytics, AI Business Insights, and Product Analytics — where the ability to deliver faster, clearer insights using AI is the differentiating skill.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/greeshmareddyn)
[![GitHub](https://img.shields.io/badge/GitHub-NGR1655-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NGR1655)

---

<div align="center">

---

*The future of business analysis is not writing better queries.*
*It is asking better questions.*

---

</div>
