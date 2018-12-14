from flask import render_template
from thinkaboutit import app
from flask_socketio import SocketIO, join_room, emit



socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print(data)
    emit('join_room', {'room': 'hi'})
