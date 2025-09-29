from flask import Flask, render_template, request, jsonify
from config import Config
from models import db
from uuid import uuid4

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

"""with app.app_context():
    db.create_all()
    if not FlashCard.query.all():
        card = FlashCard(
        question="¿Cuál es la capital de Francia?",
        answer="París"
        )
        new_card = NewFlashCard(
            front = '<h1>¿Cuál es la capital de Francia?</h1>',
            back = '<p style="background-color: red;">París</p>'
            )
        db.session.add(card)
        db.session.add(new_card)
        db.session.commit()"""


@app.route('/home/<user>', methods=['GET', 'POST'])
def welcomePage(user):
    return render_template('endpoint/user_home.html', user=user)


@app.route('/', methods=['GET', 'POST'])
def landingPage():
    if request.method == 'POST':
        json = {
            "title": "Titulo de apoyo",
            "name": "Nombre de la persona"
        }
        return jsonify(json), 201
    return render_template('home.html')


@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    if NewFlashCard.query.all():
        flashcards = NewFlashCard.query.all()
    else:
        flashcards = []
    return render_template('flashcards.html', flashcards=flashcards)

@app.errorhandler(404)
def notFound(error):
    return render_template('http/404.html', error=error)