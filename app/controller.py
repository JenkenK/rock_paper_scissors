from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import *
from app.models.add_player_choice import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-player-to-game', methods=['POST'])
def add_player_choice():
    player_1 = Player(name=request.form['player_1_name'], choice=request.form['player_1_choice'])
    player_2 = Player(name=request.form['player_2_name'], choice=request.form['player_2_choice'])
    add_player_choice_to_screen(player_1, player_2)
    game = Game()
    result = game.play(player_1, player_2)
    return render_template('index.html', players=player_choice, game_result=result)

@app.route('/welcomepage')
def welcome_page():
    return render_template('welcome_page.html')
