from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcomepage')
def welcome_page():
    return render_template('welcome_page.html')


