from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import *
from app.models.rps import *

game = Game()

@app.route('/')
def index():
    return render_template('welcome_page.html')

@app.route('/play/<player_number>')
def play(player_number):
    return render_template('play_game.html', player_number=player_number)

@app.route('/add-player/<player_number>', methods=['POST'])
def add_player_choice(player_number):
    if player_number == "1":
        game.reset_game()
    game.add_player_choice(player_number, Player(name=request.form['player_name'], choice=request.form['player_choice']))
    if game.player_1 != None and game.player_2 != None: 
        game.play()
        return redirect('/result')
    return redirect('/play/2')

@app.route('/result')
def show_result():
    return render_template('result.html', game_result=game.result, players = [game.player_1, game.player_2])

@app.route('/reset', methods=['POST'])
def reset_game():
    game.reset_game()
    return redirect('/play/1')

@app.route('/play-computer')
def render_computer_page():
    return render_template('play_computer.html')

@app.route('/play-computer', methods=['POST'])
def play_computer():
    game.add_player_choice(1, Player(name=request.form['player_name'], choice=request.form['player_choice']))
    game.add_player_choice(2, Player(name="Computer", choice= ["Rock", "Paper", "Scissors"][randint(0,2)]))
    game.play()
    return redirect('/result')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/mvp')
def render_mvp_page():
    return render_template('mvp.html')

@app.route('/mvp/<player_1_name>/<player_1_choice>/<player_2_name>/<player_2_choice>', methods=['GET'])
def mvp_index(player_1_name, player_1_choice, player_2_name, player_2_choice):
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Rps()
    result = game.play(player_1, player_2)
    return render_template('mvp.html', game_result=result)