# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import app_index
from datetime import datetime
from flask import render_template, current_app, request


@app_index.before_app_request
def log_request_data():
    current_app.logger.warning(
        "Req----Time:~~~%r --------> remote_addr = %s, url = %s, data = %r, args = %r, values = %r" %
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.remote_addr, request.url,
         request.data, request.args, request.values))


@app_index.route('/')
def index():
    return render_template('app_index/app_index.html')
