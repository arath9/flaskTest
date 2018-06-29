# app/__init__.py

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from config import app_config
from .databaseconfig import MYSQL_USER,MYSQL_PASS,DATABASE_DB,DATABASE_HOST



#db initialization
mysql = MySQL()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    #Database configs

    app.config['MYSQL_DATABASE_USER'] = MYSQL_USER
    app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_PASS
    app.config['MYSQL_DATABASE_DB'] = DATABASE_DB
    app.config['MYSQL_DATABASE_HOST'] = DATABASE_HOST

    mysql.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app
