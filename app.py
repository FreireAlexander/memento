from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        json = {
            "title": "Titulo de apoyo",
            "name": "Nombre de la persona"
        }
        return jsonify(json), 201
    return render_template('home.html')