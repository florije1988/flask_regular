# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask.ext import restful
try:
    import simplejson as json
except ImportError:
    import json
import copy
import datetime
from decimal import Decimal


class BaseHandler(restful.Resource):
    @staticmethod
    def json_output(code=0, msg='success', data=None):
        return JSONResponse(code=code, msg=msg, data=data).to_json()


class JSONResponse(object):
    def __init__(self, code=0, msg='success', data=None):
        self.code = code
        self.msg = msg
        self.data = data

    def to_json(self):
        # return simplejson.dumps(self.__to_dict(), ensure_ascii=False)
        return self.__to_dict()

    def __to_dict(self):
        re_dict = dict(code=self.code, msg=self.msg)
        if self.data:
            re_dict['data'] = self.data
        return self.__scrubbing(re_dict)

    def __scrubbing(self, x):
        """None to empty string"""
        ret = copy.deepcopy(x)
        # Handle dictionaries. Scrub all values
        if isinstance(x, dict):
            for k, v in ret.items():
                ret[k] = self.__scrubbing(v)
        elif isinstance(x, list):
            for i in xrange(len(ret)):
                ret[i] = self.__scrubbing(ret[i])
        elif isinstance(x, Decimal):  # Handle Decimal
            ret = str((Decimal(x)).quantize(Decimal('1.00')))
        elif isinstance(x, datetime.datetime):  # Handle datetime
            ret = x.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(x, datetime.time):  # Handle time
            ret = x.strftime('%H:%M')
        elif x is None:  # Handle None
            ret = ''
        return ret