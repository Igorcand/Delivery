from delivery.ext.auth import models
from delivery.ext.auth.commands import list_users, add_user

from delivery.ext.db import db 
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.admin import admin

from delivery.ext.auth.models import User

def init_app(app):
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    #pra adicionar uma view nos passamos a classe modelo da view, com os parametros do modelo da tabela e o banco de dados
    admin.add_view(UserAdmin(User, db.session))
