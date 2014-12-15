# -*- coding: utf-8 -*-
__author__ = 'florije'


class ApiBaseError(Exception):
    '''
    基异常类。
    '''

    status_code = 200
    code = 0

    def __init__(self, message, code, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message if message else ''
        self.code = code if code else self.code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

        # def to_dict(self):
        # res = dict()
        #     res['data'] = dict(self.payload or ())
        #     res['msg'] = self.message
        #     res['code'] = self.code
        #     # current_app.logger.warning('miaomiao %s' % 'name')
        #     current_app.logger.warning('Res----Time:~~~%r -------->  %r' % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        #                                                                     simplejson.dumps(res)))
        #     return res


class InvalidAPIUsage(ApiBaseError):
    code = 10000

    def __init__(self, message=None, code=None, status_code=None, payload=None):
        super(InvalidAPIUsage, self).__init__(message=message, code=code, status_code=status_code, payload=payload)