from ._config import db


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, func, Text, JSON
from uuid import uuid4


class Deck(db.Model):
    """
    id: identificador unico del deck
    name: nombre del deck
    description: pequeña descripción del contenido del mazo
    created_at: fecha de creación del mazo
    """