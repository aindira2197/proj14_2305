from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'

db = SQLAlchemy(app)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


@app.route('/')
def home():

    games = Game.query.all()

    text = ""

    for game in games:
        text += f"{game.title}<br>"

    return text


@app.route('/add/<title>')
def add(title):

    game = Game(title=title)

    db.session.add(game)
    db.session.commit()

    return "Game Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
