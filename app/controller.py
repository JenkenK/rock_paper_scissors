from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import *

game = Game()

@app.route('/')
def index():
    return render_template('welcome_page.html')

@app.route('/play')
def play():
    return render_template('play_game.html', players=game.player_choice, game_result=game.result)

@app.route('/play-game', methods=['POST'])
def add_player_choice():
    player_1 = Player(name=request.form['player_1_name'], choice=request.form['player_1_choice'])
    player_2 = Player(name=request.form['player_2_name'], choice=request.form['player_2_choice'])
    game.add_player_choice(player_1, player_2)
    game.play(player_1, player_2)
    return redirect('/play')

@app.route('/reset', methods=['POST'])
def reset_game():
    game.reset_game()
    return redirect('/play')

@app.route('/rules')
def rules():
    return render_template('rules.html')


@app.route('/about')
def about():
    return render_template('about.html')

