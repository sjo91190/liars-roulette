from flask import request, render_template, redirect, url_for
from app.main import main
from app.main.forms import PlayerNameForm, PlayerCountForm
from app.main.utils import create

config = dict()


@main.route("/", methods=['GET', 'POST'])
def index():
    form = PlayerCountForm()

    if request.method == "GET":
        return render_template("index.html", form=form)

    config['count'] = int(form.number.data)
    print(config['count'])

    return redirect(url_for("main.assign"))


@main.route("/assign", methods=['GET', 'POST'])
def assign():
    config['names'] = []
    number = config["count"]
    players = {f"player{i}": f"Player {i + 1}" for i in range(number)}

    PlayerNameForm.append_class(players)
    form = PlayerNameForm()

    if request.method == "GET":
        return render_template("assign.html", players=players, form=form)

    if request.method == "POST":
        for i in range(number):
            config['names'].append(form.data.get(f"player{i}"))

        config['liars'] = create(player_list=config['names'])
        print(config['liars'])

        return redirect(url_for("main.play"))


@main.route("/liar", methods=['GET', 'POST'])
def play():
    print('play')
    return render_template("play.html", liars=config.get('liars'))
