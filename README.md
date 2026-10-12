# TextInsight Agent

An AI agent built with [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) that analyzes a piece of text and returns its **category**, the **entities** it mentions, and a **one-sentence summary**.

## What It Does

| Step | Output | Details |
|------|--------|---------|
| **1. Classification** | `classification` | Labels the text as `News`, `Blog`, `Research`, or `Other` |
| **2. Entity Extraction** | `entities` | Finds people, organizations, and locations |
| **3. Summarization** | `description` | Writes a one-sentence summary |

Each step is a node in the graph, and the nodes run in sequence:

```
START → classification → entity_extraction → summarization → END
```

## Example

**Input**
```python
{"text": "OpenAI has announced GPT-4, a large multimodal model..."}
```

**Output**
```python
{
    "classification": "News",
    "entities": [
        {"name": "OpenAI", "entity_type": "Organization"},
        {"name": "GPT-4", "entity_type": "Other"}
    ],
    "description": "OpenAI announced GPT-4, a multimodal model focused on safety and efficiency."
}
```

## Getting Started

### Prerequisites
- Python 3.11+
- An API key for your LLM provider

### Installation
```bash
git clone <your-repo-url>
cd textinsight-agent
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration
Copy the example environment file and add your key:
```bash
cp .env.example .env
```
```env
ANTHROPIC_API_KEY=your-key-here
```
Never commit `.env` to version control.

### Run
```bash
python main.py
```

## Project Structure

```
textinsight-agent/
├── main.py              # Entry point: builds and runs the agent
├── graph.py             # Workflow: connects nodes and edges, compiles the graph
├── nodes.py             # Node functions (classify, extract, summarize)
├── state.py             # Shared state passed between nodes
├── prompts.py           # Prompt templates for each task
├── llm.py               # LLM initialization and configuration
├── pydantic_models.py   # Schemas for structured LLM output and validation
├── domain_types.py      # Shared enums and allowed values (categories, entity types)
├── settings.py          # Loads and validates configuration
└── utils.py             # Reusable helper functions
```

## How It Works

1. `main.py` sends the input text into the compiled graph from `graph.py`.
2. Each node in `nodes.py` formats a prompt from `prompts.py` and calls the LLM from `llm.py`.
3. The LLM's response is validated against the schemas in `pydantic_models.py`.
4. Each node writes its result into the shared state defined in `state.py`, so later nodes can see earlier results.
5. The final state is returned with all fields filled in.

## Customizing

- **Add a category or entity type:** update `domain_types.py` and the matching prompt in `prompts.py`.
- **Change the model:** edit `llm.py` or the model name in `settings.py`.
- **Add a new step:** write a node in `nodes.py`, register it in `graph.py`, and add its field to `state.py`.

## Tech Stack

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview): workflow orchestration
- [LangChain](https://docs.langchain.com/oss/python/langchain/overview): LLM integration
- [Pydantic](https://docs.pydantic.dev/): structured output validation