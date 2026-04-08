import json
import time
from pathlib import Path

import requests
from flask import current_app

CACHE_FILE = Path(__file__).resolve().parents[2] / "app" / "data" / "github_cache.json"
CACHE_TTL_SECONDS = 60 * 60 * 6


def _read_cache():
    try:
        if CACHE_FILE.exists():
            data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            if time.time() - data.get("timestamp", 0) < CACHE_TTL_SECONDS:
                return data.get("repos", [])
    except Exception:
        return None
    return None


def _write_cache(repos):
    try:
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(
            json.dumps({"timestamp": time.time(), "repos": repos}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except Exception:
        pass


def get_curated_projects():
    return [
        {
            "title": "Aplicações Flask e Dash para IA aplicada",
            "title_en": "Flask and Dash applications for applied AI",
            "summary": "Projetos voltados para products analytics, otimização, dashboards executivos e aplicações técnicas com foco em clareza, performance e deploy em cloud.",
            "summary_en": "Projects focused on product analytics, optimization, executive dashboards, and technical applications with clarity, performance, and cloud deployment in mind.",
            "tags": ["Flask", "Dash", "Cloud Run", "Analytics"],
        },
        {
            "title": "Modelagem, experimentação e ciência de dados",
            "title_en": "Modeling, experimentation, and data science",
            "summary": "Trilha orientada a modelagem estatística, machine learning supervisionado e não supervisionado, mensuração de impacto e experimentação orientada a negócio.",
            "summary_en": "Track focused on statistical modeling, supervised and unsupervised machine learning, impact measurement, and business-oriented experimentation.",
            "tags": ["Machine Learning", "PySpark", "MLOps", "Statistics"],
        },
        {
            "title": "Sistemas embarcados, IoT e programação em tempo real",
            "title_en": "Embedded systems, IoT, and real-time programming",
            "summary": "Projetos que conectam ESP32, RTOS, sensores, atuadores, automação e arquitetura de sistemas embarcados com forte viés didático e experimental.",
            "summary_en": "Projects connecting ESP32, RTOS, sensors, actuators, automation, and embedded systems architecture with a strong didactic and experimental approach.",
            "tags": ["ESP32", "RTOS", "IoT", "Embedded"],
        },
    ]


def _fallback_repos(username):
    return [
        {
            "name": "tekforge-showcase",
            "description": "Estrutura base do portfólio técnico em Flask, com currículo, projetos, sala de aula e páginas bilíngues.",
            "url": f"https://github.com/{username}",
            "language": "Python",
            "stars": 0,
            "score": 0,
        },
        {
            "name": "applied-ml-lab",
            "description": "Exemplo de organização para modelos, notebooks, métricas e deploy de aplicações orientadas a IA aplicada.",
            "url": f"https://github.com/{username}",
            "language": "Python",
            "stars": 0,
            "score": 0,
        },
    ]


def get_featured_repositories(force_refresh=False):
    username = current_app.config["GITHUB_USERNAME"]
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=24"
    curated = {
        "ml": ["machine", "ml", "model", "catboost", "cluster", "rag", "vision", "ai"],
        "education": ["edu", "class", "notebook", "streamlit", "teaching", "course"],
        "robotics": ["esp32", "robot", "iot", "rtos", "embedded", "sensor"],
        "software": ["flask", "dash", "api", "cloud", "app", "deploy"],
    }

    if not force_refresh:
        cached = _read_cache()
        if cached:
            return cached

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"Accept": "application/vnd.github+json", "User-Agent": "tekforge-portfolio"},
        )
        response.raise_for_status()
        repos = response.json()

        items = []
        for repo in repos:
            name = (repo.get("name") or "").lower()
            description = (repo.get("description") or "").lower()
            text = f"{name} {description}"
            score = 0
            for keywords in curated.values():
                if any(keyword in text for keyword in keywords):
                    score += 3
            if repo.get("stargazers_count", 0):
                score += 1
            if not repo.get("fork", False):
                score += 1
            if repo.get("homepage"):
                score += 1

            items.append(
                {
                    "name": repo.get("name"),
                    "description": repo.get("description") or "Technical repository published on GitHub.",
                    "url": repo.get("html_url"),
                    "language": repo.get("language") or "N/A",
                    "stars": repo.get("stargazers_count", 0),
                    "score": score,
                    "updated_at": repo.get("updated_at"),
                }
            )

        items = sorted(items, key=lambda x: (x["score"], x["stars"], x["updated_at"] or ""), reverse=True)
        items = items[:9]
        _write_cache(items)
        return items
    except Exception:
        cached = _read_cache()
        return cached or _fallback_repos(username)
