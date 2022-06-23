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

    @app.cli.command()
    def listar_usuarios():
        users = User.query.all()
        click.echo( f'lista de usuarios: {users}')

    @app.cli.command()
    @click.option('--email', '-e')
    @click.option('--passwd', '-p')
    @click.option('--admin', '-a', is_flag=True, default=False)
    def add_user(email, passwd, admin):
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo( f'Usuario {email} criado com sucesso!')