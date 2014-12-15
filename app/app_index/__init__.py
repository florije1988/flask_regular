# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint

app_index = Blueprint('app_index', __name__, static_folder='static', template_folder='templates')

from . import views