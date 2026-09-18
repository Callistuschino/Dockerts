import os
import socket
import sys
import time
from datetime import datetime, timezone
from flask import Flask, jsonify

START_TIME = time.time()


def create_app(test_config=None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    @app.route("/", methods=["GET"])
    def root():
        return jsonify({
            "name": "dockerts",
            "message": "Welcome to the Dockerts Python service!",
            "version": "0.1.0",
            "status": "running",
            "endpoints": [
                "/",
                "/health",
                "/info"
            ]
        })

    @app.route("/health", methods=["GET"])
    def health():
        uptime = round(time.time() - START_TIME, 2)
        return jsonify({
            "status": "healthy",
            "uptime_seconds": uptime,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }), 200

    @app.route("/info", methods=["GET"])
    def info():
        return jsonify({
            "hostname": socket.gethostname(),
            "python_version": sys.version.split()[0],
            "platform": sys.platform,
            "environment": os.getenv("APP_ENV", "production")
        }), 200

    return app


app = create_app()


def main():
    """Application entry point for running the server."""
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    debug = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")

    print(f"Starting Dockerts server on {host}:{port} (debug={debug})...")
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
