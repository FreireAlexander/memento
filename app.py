from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, FlashCard
from uuid import uuid4

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    if not FlashCard.query.all():
        card = FlashCard(
        question="¿Cuál es la capital de Francia?",
        answer="París"
        )
        db.session.add(card)
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        json = {
            "title": "Titulo de apoyo",
            "name": "Nombre de la persona"
        }
        return jsonify(json), 201
    return render_template('home/base.html')


@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    if FlashCard.query.all():
        flashcards = FlashCard.query.all()
    else:
        flashcards = []
    return render_template('flashcards.html', flashcards=flashcards)