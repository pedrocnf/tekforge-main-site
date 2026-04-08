from flask import Blueprint, render_template, request
from app.services.github_service import get_curated_projects, get_featured_repositories

projects_bp = Blueprint("projects", __name__)


def get_lang():
    lang = request.args.get("lang", "pt")
    return lang if lang in {"pt", "en"} else "pt"


def tr(lang, pt, en):
    return pt if lang == "pt" else en


@projects_bp.route("/")
def list_projects():
    lang = get_lang()
    repos = get_featured_repositories()
    curated = get_curated_projects()
    ui = {
        "title": tr(lang, "Projetos", "Projects"),
        "subtitle": tr(lang, "Acesse projetos em destaque, frentes técnicas e repositórios atualizados a partir do GitHub.", "Access featured projects, technical tracks, and repositories updated from GitHub."),
        "featured_title": tr(lang, "Curadoria técnica", "Technical curation"),
        "featured_subtitle": tr(lang, "Use esta seleção para entender o tipo de problema, tecnologia e entrega presente na plataforma.", "Use this selection to understand the type of problem, technology, and delivery present on the platform."),
        "live_title": tr(lang, "Repositórios do GitHub", "GitHub repositories"),
        "live_subtitle": tr(lang, "Veja os repositórios mais relevantes com atualização dinâmica a partir do GitHub.", "Review the most relevant repositories with dynamic updates from GitHub."),
        "empty_title": tr(lang, "Nenhum repositório disponível", "No repositories available"),
        "empty_text": tr(lang, "Verifique o usuário do GitHub configurado no ambiente.", "Check the GitHub username configured in the environment."),
        "cta": tr(lang, "Abrir no GitHub", "Open on GitHub"),
    }
    return render_template("projects.html", repos=repos, curated=curated, lang=lang, current_lang=lang, ui=ui)
