from ._config import db


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, func, Text, JSON
from uuid import uuid4


class FlashCard(db.Model):
    id = Column(String, primary_key=True,  default=lambda: str(uuid4().hex))
    question = Column(String(200), nullable=False)
    answer = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    """
    id = Column(String, primary_key=True,  default=lambda: str(uuid4().hex))
    front = Column(Text, nullable=False)
    back = Column(Text, nullable=False)
    validatio = Column(Text, nullable=False)
    fields = Column(JSON, nullable=False)
    """