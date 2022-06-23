from delivery.ext.auth.models import User
from delivery.ext.db import models 
from delivery.ext.db import db
import click

    
    
def list_users():
    users = User.query.all()
    click.echo( f'lista de usuarios: {users}')


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