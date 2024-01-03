from flask import Blueprint, render_template
import random

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template('homepage.html')

@views.route('/games')
def games():
    return render_template('gamepage.html')

# To be completed with templates for each of the 6 games.
@views.route('/games/reactionTime')
def reactionTime():
    return

@views.route('/games/sequenceMemory')
def sequenceMemory():
    return

@views.route('/games/game3')
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
