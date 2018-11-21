from flask import render_template
from thinkaboutit import app

@app.route('/')
def index():
    return 'Hello'
