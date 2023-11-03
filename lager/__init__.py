import os

from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import DevConfig, ProdConfig 
from .forms import InsertForm, ChangeForm, SearchForm

db = SQLAlchemy()
ma = Marshmallow()


class Ware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lagerplatz = db.Column(db.Integer, nullable=False)
    produktname = db.Column(db.String(200), nullable=False)
    kategorie = db.Column(db.String(200))
    preis = db.Column(db.Float)
    designer = db.Column(db.String(200))
    label = db.Column(db.String(200))
    ausziehbar = db.Column(db.Boolean)
    klappbar = db.Column(db.Boolean)
    
    


class WareSchema(ma.Schema):
    class Meta:
        fields = ("id", "lagerplatz", "produktname", "kategorie", "preis", "designer", "label", "ausziehbar", "klappbar")
        
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("ware_detail", values=dict(id="<id>")),
            "collection": ma.URLFor("wares"),
        }
    )


ware_schema = WareSchema()
wares_schema = WareSchema(many=True)


def create_app(config_class=ProdConfig):

    app = Flask(__name__)
    app.config.from_object(ProdConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()  

    from .routes import ware_bp
    app.register_blueprint(ware_bp)

    return app







        