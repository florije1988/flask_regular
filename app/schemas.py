# -*- coding: utf-8 -*-
__author__ = 'florije'
from . import ma


class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'content')