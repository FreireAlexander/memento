from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


db = SQLAlchemy()


class FlashCard(db.Model):
    id = db.Column(db.String, primary_key=True,  default=lambda: str(uuid4().hex))
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    