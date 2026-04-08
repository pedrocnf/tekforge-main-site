import os
from dotenv import load_dotenv

load_dotenv()


def _as_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tekforge-dev-secret")
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "pedrocnf")
    SITE_TITLE = os.getenv("SITE_TITLE", "TekForge")
    SITE_DOMAIN = os.getenv("SITE_DOMAIN", "tekforge.com.br")
    SITE_SUBTITLE = os.getenv(
        "SITE_SUBTITLE",
        "TekForge é um hub de tecnologia que reúne perfil profissional, projetos, materiais de ensino e aplicações.",
    )
    SITE_URL = os.getenv("SITE_URL", "https://tekforge.com.br")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    APP_VERSION = os.getenv("APP_VERSION", "v12-deploy")
    FLASK_DEBUG = _as_bool(os.getenv("FLASK_DEBUG"), default=False)
    GITHUB_CACHE_TTL_SECONDS = int(os.getenv("GITHUB_CACHE_TTL_SECONDS", "900"))
