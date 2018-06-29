# views.py

import os

from . import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route('/')
def index():
    return 'Hola soy el index'

@app.route('/about')
def about():
    return 'Hola soy el about'