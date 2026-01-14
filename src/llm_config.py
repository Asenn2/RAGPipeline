# src/llm_config.py
from crewai import LLM

llama3_llm = LLM(
    model="ollama/llama3",
    api_base="http://localhost:11434",
    temperature=0.1,
    max_tokens=512
)