# -*- coding: utf-8 -*-
__author__ = 'florije'
import json
from datetime import datetime

from flask.ext import restful
from flask import make_response, current_app

from .custom_exception import ApiBaseError


settings = {}


class Api(restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'application/json': self.output_json,
        }

    def handle_error(self, error):
        code = getattr(error, 'code', 500)
        if issubclass(error.__class__, ApiBaseError):
            response = {
                'code': code,
                'msg': 'Server raise error: %s' % (error.message,),
                'data': {}
            }
            current_app.logger.warning('Res----Time:~~~%r -------->  %r'
                                       % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), response))
            return self.make_response(response, 200)
        if code:
            response = {
                'code': -1,
                'msg': 'Status_code: %s ,Server raise error: %s' % (code, error),
                'data': {}
            }
            current_app.logger.warning('Res----Time:~~~%r -------->  %r'
                                       % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), response))
            return self.make_response(response, 200)
        return super(Api, self).handle_error(error)

    @staticmethod
    def output_json(data, code, headers=None):
        """Makes a Flask response with a JSON encoded body"""

        local_settings = settings.copy()
        dumped = json.dumps(data, **local_settings)
        if 'indent' in local_settings:
            dumped += '\n'

        resp = make_response(dumped, code)
        resp.headers.extend(headers or {})
        current_app.logger.warning('Res----Time:~~~%r -------->  %r'
                                   % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data))
        return resp