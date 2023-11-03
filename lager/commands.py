import click
from flask.cli import with_appcontext
from .models import db, Ware  # Assuming your models are in a separate file named models.py
from .filldb import insert_Ware

@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database.')

@click.command('insert-ware')
@with_appcontext
def insert_ware_command():
    insert_Ware(db)
    click.echo('Inserted Ware data.')

def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(insert_ware_command)
