from email.policy import default
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models 
import click

def init_app(app):
    @app.cli.command()
    def create_db():
        '''Este comando inicializa o banco de dados'''
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        #TODO:Usar tabulate
        click.echo('lista de pedidos')

    

    