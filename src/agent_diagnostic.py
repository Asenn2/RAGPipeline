# src/agent_diagnostic.py
from crewai import Agent
from .llm_config import llama3_llm

diagnostic_agent = Agent(
    role="Médecin IA",
    goal="Analyser un rapport médical et dire en français s'il est cancéreux ou non, en JSON strict.",
    backstory=(
        "Tu es un médecin spécialisé en oncologie. Tu lis des rapports médicaux "
        "et donnes un diagnostic clair sur la présence ou non de cancer. "
        "**Toujours répondre uniquement en JSON.**"
    ),
    llm=llama3_llm,
    verbose=True,
)