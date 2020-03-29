from flask import render_template, request
from flask_socketio import SocketIO, join_room, emit
from thinkaboutit import app
import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

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
