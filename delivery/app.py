from flask import Flask
from delivery.ext import site 
from delivery.ext import toolbar
from delivery.ext import config
from delivery.ext import db
from delivery.ext import cli
from delivery.ext import migrate
from delivery.ext import hooks
from delivery.ext import auth



def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()