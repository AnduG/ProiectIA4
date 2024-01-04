from flask import Blueprint, render_template
from flask_login import current_user
import random

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    if current_user.is_authenticated:
        return render_template('user-homepage.html')
    else:
        return render_template('homepage.html')
        

@views.route('/games')
def games():
    return render_template('gamepage.html')

# To be completed with templates for each of the 6 games.
@views.route('/games/reactionTime')
def reactionTime():
    return

@views.route('/games/sequenceMemory', methods=['GET', 'POST'])
def sequenceMemory():
    return render_template("sequence-startscreen.html")

@views.route('/games/sequenceMemoryRunGame')
def displayPattern():
    return render_template("sequence-run-game.html")

@views.route('/games/wordGeneration')
def game3():
    return

@views.route('/games/game4')
def game4():
    return

@views.route('/games/game5')
def game5():
    return

@views.route('/games/game6')
def game6():
    return
