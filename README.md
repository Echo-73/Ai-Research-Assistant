# AI Research Assistant

An AI-powered multi-agent research assistant built using CrewAI, Groq LLMs, Streamlit, and Serper Search.

## Features

* Automated web research using Serper Search API
* Multi-agent collaboration with CrewAI
* Research Specialist agent for information gathering
* Data Analyst agent for extracting insights and trends
* Content Writer agent for generating structured reports
* Streamlit-based interactive user interface
* Groq-powered fast LLM inference

## Tech Stack

* Python
* CrewAI
* CrewAI Tools
* Groq API
* Serper API
* Streamlit
* LiteLLM

## Project Structure

```
ai-research-assistant/
│
├── agents/
│   ├── research_specialist.py
│   ├── data_analyst.py
│   └── content_writer.py
│
├── tasks/
│   ├── research_task.py
│   ├── analysis_task.py
│   └── writing_task.py
│
├── crew.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository

```bash
git clone <repo-url>
cd ai-research-assistant
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the environment

```bash
.venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file

```env
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key

RESEARCH_AGENT_LLM=groq/llama-3.1-8b-instant
ANALYST_AGENT_LLM=groq/llama-3.3-70b-versatile
WRITER_AGENT_LLM=groq/llama-3.3-70b-versatile

RESEARCH_AGENT_TEMPERATURE=0.1
ANALYST_AGENT_TEMPERATURE=0.2
WRITER_AGENT_TEMPERATURE=0.3
```

6. Run the application

```bash
streamlit run app.py
```

## Future Improvements

* PDF report export
* Research history database
* RAG integration
* Multi-language support
* Citation validation
