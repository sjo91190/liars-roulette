"""
Views and routes for roulette
"""
import random
from os import path
from flask import request, render_template, redirect, url_for, session
from app.main import main
from app.main.forms import PlayerNameForm, PlayerCountForm
from app.main.utils import img_builder, Player

img_root = path.split(__file__)[0][:-4] + "static/img"
images = img_builder(img_root)


@main.route("/", methods=['GET', 'POST'])
def index():
    """
    Index page where user selects the amount of players
    Form used limits to 6 players
    :return: Returns index template if GET, assign template if POST
    """
    form = PlayerCountForm()

    if request.method == "GET":
        return render_template("index.html", form=form)

    session['count'] = int(form.number.data)
    return redirect(url_for("main.assign"))


@main.route("/assign", methods=['GET', 'POST'])
def assign():
    """
    Player names created and Player objects created
    :return: assign template of GET, play if POST
    """
    number = session.get('count')
    players = {f"player{i}": f"Player {i + 1}" for i in range(number)}

    PlayerNameForm.append_class(players)
    form = PlayerNameForm()

    if request.method == "GET":
        return render_template("assign.html", players=players, form=form)

    if request.method == "POST":

        session['names'] = [form.data.get(f"player{i}") for i in range(number)]
        session['players'] = {name: Player(name).to_dict() for name in session['names']}
        session['profile'] = dict(zip(session.get('names'), random.sample(images, number)))

        return redirect(url_for("main.play"))


@main.route("/liar", methods=['GET', 'POST'])
def play():
    """
    Main game loop. Player selected undergoes a roll and stats are updated
    :return: returns play for GET and POST
    """

    player_data = session['players']
    players = {name: Player.from_dict(data) for name, data in player_data.items()}

    if request.method == "GET":
        return render_template("play.html", liars=player_data, pfp=session.get('profile'))

    person = request.form.get('person')
    players[person].roll()

    session['players'] = {name: data.to_dict() for name, data in players.items()}

    return redirect(url_for("main.play"))
