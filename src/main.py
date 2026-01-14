# src/main.py
import os
from crewai import Crew
from src.task_diagnostic import diagnostic_task  # ← Ajoutez "src." au début

def lire_fichier(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path_rapport = os.path.join(base_dir, "data", "rapport1.txt")
    texte = lire_fichier(path_rapport)

    task = diagnostic_task(texte)
    crew = Crew(agents=[task.agent], tasks=[task], verbose=True)

    result = crew.kickoff()
    print("\n=== Résultat du diagnostic ===\n")
    print(result)