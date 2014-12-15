# -*- coding: utf-8 -*-
__author__ = 'florije'
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.marshmallow import Marshmallow

from config import config


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    # app = ResponsiveFlask(__name__)
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # print app.config.get('HOST')

    db.init_app(app)
    ma.init_app(app=app)

    # main module
    from app_todo import app_todo as app_todo_blueprint
    from app_index import app_index as app_index_blueprint

    app.register_blueprint(app_todo_blueprint, url_prefix='/todo')  # url_prefix='/task'
    app.register_blueprint(app_index_blueprint, )

    handler = TimedRotatingFileHandler(
        filename='{0}/{1}'.format(app.config.get('LOG_PATH'), app.config.get('LOG_NAME')), when='D',
        interval=1, backupCount=5)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.debug = app.config.get('APP_DEBUG')

    return app