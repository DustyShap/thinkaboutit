import os

from flask import Flask
from flask_socketio import SocketIO

from models import db

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    socketio = SocketIO(app)
    return app


def main():
    db.create_all()


if __name__ == '__main__':
    with create_app().app_context():
        main()
