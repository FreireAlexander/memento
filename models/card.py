from ._config import db


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, func, Text, JSON
from uuid import uuid4


class Card(db.Model):  
    """
    id: valor de identificación único
    fields: valores de los campos a renderizar y que deben venir de la definición de estos en en el cardModel
    srs_data: spaced repetition system data, variables para el sistema de repetición espaciada

    created_at: fecha de creación
    foreing keys:
    """

    