# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint
from app.custom_api import Api

app_todo = Blueprint('app_task', __name__)
api_todo = Api(app_todo, catch_all_404s=True)

from . import views

api_todo.add_resource(views.HelloHandler, '/hello')