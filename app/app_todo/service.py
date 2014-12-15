# -*- coding: utf-8 -*-
__author__ = 'florije'
from ..basic_service import BaseService
from app.models import TodoModel
from app.schemas import TodoSchema
from app.custom_exception import InvalidAPIUsage


class TodoService(BaseService):
    def create_task(self, **params):
        new_task = TodoModel(title=params.get('title'), content=params.get('content'))
        self.db.add(new_task)
        self.flush()
        task_ma = TodoSchema().dump(new_task)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data

    @staticmethod
    def get_tasks():
        res_task = TodoModel.query.all()
        task_ma = TodoSchema().dump(res_task, many=True)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data

    @staticmethod
    def get_task_by_id(task_id):
        res_task = TodoModel.query.filter(TodoModel.id == task_id).first()
        task_ma = TodoSchema().dump(res_task)
        if task_ma.errors:
            raise InvalidAPIUsage(message=task_ma.errors)
        return task_ma.data