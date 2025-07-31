from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration placeholder (intentionally minimal for review)
    app.config.setdefault("WORDS_PER_MINUTE", 200)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app
