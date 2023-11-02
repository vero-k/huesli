import os

from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow



from .config import DevConfig 
from .forms import InsertForm, ChangeForm, SearchForm

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app(config_class=DevConfig):

    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)

    # Register blueprints, CLI commands, etc.
    from .commands import init_app as init_commands
    init_commands(app)

    migrate.init_app(app, db)
    ma.init_app(app)

    from .routes import ware_bp
    app.register_blueprint(ware_bp)

    return app







        