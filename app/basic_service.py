# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import db


class BaseService(object):

    def __enter__(self):
        self.db = db.session
        return self

    def __exit__(self, type, value, traceback):
        if isinstance(type, Exception):
            self.db.rollback()
        else:
            self.db.commit()
        self.db.close()

    def flush(self):
        self.db.flush()