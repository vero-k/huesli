from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SelectField, DecimalField, BooleanField, validators, SubmitField, FieldList




class InsertForm(FlaskForm):
    lagerplatz = IntegerField('lagerplatz', [validators.Length(min=0, max=6)])
    produktname = StringField('produktname', [validators.Length(min=0, max=200)])
    kategorie = SelectField('kategorie', choices=[("default", "Select"), ("Stuhl", "Stuhl"), ("Bett", "Bett"), ("Regal", "Regal"), ("Sofa", "Sofa"), ("Schrank", "Schrank"), ("Sessel", "Sessel"), ("Tisch", "Tisch"), ("Bank", "Bank")])
    designer = StringField('designer', [validators.Length(min=0, max=200)])
    label = StringField('label', [validators.Length(min=0, max=200)])
    preis = DecimalField('preis', [validators.Length(min=0, max=200)])
    ausziehbar = BooleanField('ausziehbar', )
    klappbar = BooleanField('klappbar', )
    submit = SubmitField('Submit')
    
    
class ChangeForm(FlaskForm):
    lagerplatz = IntegerField('lagerplatz', [validators.Length(min=0, max=6)])
    produktname = StringField('produktname', [validators.Length(min=0, max=200)])
    kategorie = SelectField('kategorie', choices=[("Stuhl", "Stuhl"), ("Bett", "Bett"), ("Regal", "Regal"), ("Sofa", "Sofa"), ("Schrank", "Schrank"), ("Sessel", "Sessel"), ("Tisch", "Tisch"), ("Bank", "Bank")])
    designer = StringField('designer', [validators.Length(min=0, max=200)])
    label = StringField('label', [validators.Length(min=0, max=200)])
    preis = DecimalField('preis', [validators.Length(min=0, max=200)])
    ausziehbar = BooleanField('ausziehbar', )
    klappbar = BooleanField('klappbar', )
    
        
class SearchForm(FlaskForm):
    searchfield = StringField('searchfield', [validators.Length(min=0, max=200)])
    lagerplatz = IntegerField('lagerplatz', [validators.Length(min=0, max=6)])
    produktname = StringField('produktname', [validators.Length(min=0, max=200)])
    kategorie = SelectField('kategorie', choices=[("default", "Select"), ("Stuhl", "Stuhl"), ("Bett", "Bett"), ("Regal", "Regal"), ("Sofa", "Sofa"), ("Schrank", "Schrank"), ("Sessel", "Sessel"), ("Tisch", "Tisch"), ("Bank", "Bank")])
    designer = StringField('designer', [validators.Length(min=0, max=200)])
    label = StringField('label', [validators.Length(min=0, max=200)])
    preismin = DecimalField('preismin', [validators.Length(min=0, max=200)])
    preismax = DecimalField('preismin', [validators.Length(min=0, max=200)])
    ausziehbar = BooleanField('ausziehbar', )
    klappbar = BooleanField('klappbar', )
    submit = SubmitField('Submit')
    
    
    
    
    