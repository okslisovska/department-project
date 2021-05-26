from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app


from app import routes
