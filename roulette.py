import os
from waitress import serve
from paste.translogger import TransLogger
from app import app_factory

if os.environ.get("LIARS_CONFIG") == "prod":
    if __name__ == "__main__":
        host = os.environ.get("HOST") or "0.0.0.0"
        port = os.environ.get("PORT") or 80
        app = app_factory(config_name="prod")
        serve(TransLogger(app), host=host, port=port)

else:
    app = app_factory(config_name="develop")
    host = os.environ.get("HOST") or "localhost"
    port = os.environ.get("PORT") or 5000
    serve(TransLogger(app), host=host, port=port)
