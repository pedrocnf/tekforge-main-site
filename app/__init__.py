from flask import Flask, request, render_template
from .routes.main import main_bp
from .routes.projects import projects_bp
from .routes.teaching import teaching_bp
from .routes.api import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(teaching_bp, url_prefix="/teaching")
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.context_processor
    def inject_site_config():
        lang = request.args.get("lang", "pt")
        if lang not in {"pt", "en"}:
            lang = "pt"
        labels = {
            "pt": {
                "home": "Início",
                "resume": "Currículo",
                "projects": "Projetos",
                "teaching": "Sala de Aula",
                "lab": "Lab",
                "contact": "Contato",
            },
            "en": {
                "home": "Home",
                "resume": "Resume",
                "projects": "Projects",
                "teaching": "Classroom",
                "lab": "Lab",
                "contact": "Contact",
            },
        }
        return {
            "site_title": app.config.get("SITE_TITLE", "TekForge"),
            "site_subtitle": app.config.get("SITE_SUBTITLE", "TekForge"),
            "site_domain": app.config.get("SITE_DOMAIN", "tekforge.com.br"),
            "site_url": app.config.get("SITE_URL", "https://tekforge.com.br"),
            "current_lang": lang,
            "nav_labels": labels[lang],
            "current_year": 2026,
        }

    @app.errorhandler(404)
    def not_found(error):
        lang = request.args.get("lang", "pt")
        if lang not in {"pt", "en"}:
            lang = "pt"
        return render_template("404.html", current_lang=lang), 404

    return app
