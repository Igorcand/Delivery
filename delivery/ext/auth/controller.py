from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

from delivery.ext.auth.models import User
from delivery.ext.db import db

from flask import current_app as app

ALG = 'pbkdf2:sha256'

def create_user(email:str, password:str, admin:bool=False) -> User:
    password = generate_password_hash(password, ALG)
    user = User(email=email, passwd=password, admin=admin)
    db.session.add(user)
    #TODO: Tratar exception quando o usuario ja existir
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    filename = os.path.join(
        app.config['UPLOAD_FOLDER'], 
        secure_filename(filename)
    )
    filestorage.save(filename)