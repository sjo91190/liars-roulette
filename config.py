import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    HOST = os.environ.get("HOST") or "0.0.0.0"
    PORT = os.environ.get("PORT") or 80


class DevelopmentConfig(Config):
    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST") or "localhost"
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT") or 5000
    DEBUG = True


config = {
    "develop": DevelopmentConfig,
    "prod": ProductionConfig
}
