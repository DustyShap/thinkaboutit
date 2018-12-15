from flask import render_template
from flask_socketio import SocketIO, join_room, emit
from thinkaboutit import app
import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print(data)
    emit('join_room', {'room': 'hi'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
