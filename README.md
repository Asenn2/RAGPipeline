# RAGPipeline - Système de Diagnostic Médical IA

## 📋 Description

RAGPipeline est un projet d'intelligence artificielle médicale utilisant **CrewAI** et **LLaMA 3** pour analyser des rapports médicaux et déterminer la présence ou non de cancer. Le système utilise un agent IA spécialisé en oncologie qui lit des rapports médicaux et fournit un diagnostic clair au format JSON.

### Fonctionnalités

- 🔍 Analyse automatique de rapports médicaux
- 🤖 Agent IA spécialisé en oncologie
- 📊 Résultats au format JSON structuré
- 🔬 Justification détaillée du diagnostic
- 🌐 Utilisation de LLaMA 3 via Ollama (local)

## 🔧 Prérequis

Avant d'installer le projet, assurez-vous d'avoir :

- **Python 3.8+** installé sur votre système
- **Ollama** installé et configuré ([https://ollama.ai](https://ollama.ai))
- Le modèle **LLaMA 3** téléchargé via Ollama
- **pip** pour la gestion des dépendances Python

### Installation d'Ollama et LLaMA 3

1. Installez Ollama depuis [https://ollama.ai](https://ollama.ai)
2. Téléchargez le modèle LLaMA 3 :
   ```bash
   ollama pull llama3
   ```
3. Vérifiez que le service Ollama est en cours d'exécution :
   ```bash
   ollama serve
   ```

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Asenn2/RAGPipeline.git
cd RAGPipeline
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv EnvLLM
```

### 3. Activer l'environnement virtuel

**Sur Linux/MacOS :**
```bash
source EnvLLM/bin/activate
```

**Sur Windows :**
```bash
EnvLLM\Scripts\activate
```

### 4. Installer les dépendances

```bash
pip install -r EnvLLM/requirements.txt
```

## 🚀 Utilisation

### Exécution du programme principal

Pour analyser un rapport médical :

```bash
python -m src.main
```

Le programme analysera par défaut le fichier `data/rapport1.txt` et affichera le diagnostic au format JSON.

### Exemple de sortie

```json
{
  "cancer": true,
  "justification": "Le rapport indique la présence de cellules malignes de type adénocarcinome pulmonaire confirmé par biopsie, avec une masse suspecte de 3,2 cm au scanner thoracique."
}
```

### Analyser un autre rapport

Pour analyser un rapport différent, modifiez le chemin dans `src/main.py` :

```python
path_rapport = os.path.join(base_dir, "data", "votre_rapport.txt")
```

## 📁 Structure du projet

```
RAGPipeline/
├── data/                          # Données d'exemple
│   ├── rapport1.txt              # Rapport médical cancéreux
│   ├── rapport1 - cancéreux.txt  # Exemple de rapport positif
│   └── rapport1 - non cancéreux.txt  # Exemple de rapport négatif
├── src/                          # Code source
│   ├── __init__.py              # Module Python
│   ├── main.py                  # Point d'entrée principal
│   ├── agent_diagnostic.py      # Définition de l'agent IA médical
│   ├── task_diagnostic.py       # Définition de la tâche de diagnostic
│   └── llm_config.py           # Configuration du modèle LLaMA 3
├── EnvLLM/                      # Environnement virtuel
│   └── requirements.txt         # Dépendances Python
├── LLM.pdf                      # Documentation (optionnelle)
└── README.md                    # Ce fichier
```

## 🔍 Détails techniques

### Agent IA

L'agent `diagnostic_agent` est configuré avec :
- **Rôle** : Médecin IA spécialisé en oncologie
- **Objectif** : Analyser un rapport médical et déterminer la présence de cancer
- **LLM** : LLaMA 3 (température: 0.1, max_tokens: 512)

### Configuration du LLM

Le modèle est configuré dans `src/llm_config.py` :
- **Modèle** : ollama/llama3
- **API Base** : http://localhost:11434
- **Température** : 0.1 (pour des réponses déterministes)
- **Max Tokens** : 512

### Format de sortie

Le système renvoie un JSON avec deux clés :
- `cancer` : boolean (true/false)
- `justification` : string (explication du diagnostic)

## 🛠️ Personnalisation

### Modifier la configuration du LLM

Éditez `src/llm_config.py` pour ajuster :
- La température (créativité du modèle)
- Le nombre maximum de tokens
- L'URL de l'API Ollama

### Ajouter de nouveaux rapports

Placez vos fichiers de rapport médical dans le dossier `data/` et modifiez le chemin dans `src/main.py`.

## 📝 Exemples de rapports

Le projet inclut trois exemples de rapports médicaux dans le dossier `data/` :
- `rapport1.txt` : Cas d'adénocarcinome pulmonaire (cancer)
- `rapport1 - cancéreux.txt` : Autre exemple de rapport positif
- `rapport1 - non cancéreux.txt` : Exemple de rapport négatif

## ⚠️ Avertissement

Ce projet est à but éducatif et de démonstration uniquement. Il ne doit **PAS** être utilisé pour des diagnostics médicaux réels. Consultez toujours un professionnel de santé qualifié pour tout diagnostic médical.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est fourni tel quel à des fins éducatives.

## 👤 Auteur

**Asenn2**

---

*Développé avec ❤️ en utilisant CrewAI et LLaMA 3*
