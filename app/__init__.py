from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as main_bp
    from app.main import bp as api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    return app
