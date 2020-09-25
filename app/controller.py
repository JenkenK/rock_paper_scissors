from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html')