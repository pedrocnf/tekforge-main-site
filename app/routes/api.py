from flask import Blueprint, jsonify, current_app

api_bp = Blueprint("api", __name__)


@api_bp.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "application": "tekforge",
        "version": current_app.config.get("APP_VERSION", "unknown"),
        "environment": current_app.config.get("ENVIRONMENT", "unknown"),
    })


@api_bp.route("/ready")
def ready():
    return jsonify({"status": "ready"})
