from ._config import db


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, func, Text, JSON
from uuid import uuid4


class User(db.Model):
    """
    id: identificador unico del usuario
    name: nombre del usuario
    last_name: apellido del usuario
    nickname: apodo del usuario
    email: correo del usuario
    password: contraseña del usario hasheada

    other_info: otra información que podría ser interesante completar en el perfil del usuario
    """