# src/task_diagnostic.py
from crewai import Task
from .agent_diagnostic import diagnostic_agent

def diagnostic_task(report_text):
    return Task(
        description=(
            f"Voici un rapport médical :\n\n{report_text}\n\n"
            "Tu dois déterminer s'il est question d'un cancer ou non. "
            "Ta réponse **doit être un JSON clair** avec ces clés :\n"
            '{\n'
            '  "cancer": true/false,\n'
            '  "justification": "..."  # explique pourquoi\n'
            '}'
        ),
        expected_output='Un JSON avec "cancer" (true/false) et une "justification".',
        agent=diagnostic_agent,
    )