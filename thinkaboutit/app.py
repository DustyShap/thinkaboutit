from flask import render_template, request
from flask_socketio import SocketIO, join_room, emit
#from thinkaboutit import app
from models import db, User
from create import create_app
import os

app = create_app()
socketio = SocketIO(app)
app.app_context().push()

PHONES = ['android', 'blackberry', 'iphone']

@app.route('/')
def index():
    agent = request.headers.get('User-Agent')
    if any(phone in agent.lower() for phone in PHONES):
        return render_template('index.html', mobile=True)
    else:
        return render_template('index.html', mobile=False)

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print(data)
    emit('join_room', {'room': 'hi'})
