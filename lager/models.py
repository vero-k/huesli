
from lager import db

from lager import ma



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