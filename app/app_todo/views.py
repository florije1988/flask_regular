# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import request
from flask.ext.restful import reqparse

from service import TodoService
from ..basic_handler import BaseHandler
from app.custom_exception import InvalidAPIUsage


class HelloHandler(BaseHandler):
    def get(self):
        return self.json_output({'hello': 'fuboqing'})


class TodosHandler(BaseHandler):
    def get(self):
        if not request.args:
            raise InvalidAPIUsage(message='Request data type is error!')

        parser = reqparse.RequestParser()
        parser.add_argument('task_id', type=str, required=True, help="task_id cannot be blank!", location='args')
        args = parser.parse_args()

        task_id = args.get('task_id')
        with TodoService() as task_service:
            res_task = task_service.get_task_by_id(task_id=task_id)

        if not res_task:
            # raise InvalidAPIUsage(message='task_id for {task_id} is not exist!'.format(task_id=task_id))
            return self.json_output(data={})
        return self.json_output(data=res_task)

    def post(self):
        if not request.data:
            raise InvalidAPIUsage(message='Request data type is error!')

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="title cannot be blank!", location='json')
        parser.add_argument('content', type=str, required=True, help="content cannot be blank!", location='json')
        args = parser.parse_args()

        with TodoService() as task_service:
            new_task = task_service.create_task(**args)

        return self.json_output(data=new_task)


class TaskListHandler(BaseHandler):
    def get(self):
        with TodoService() as task_service:
            res_task = task_service.get_tasks()

        if not res_task:
            return self.json_output(data={})
        return self.json_output(data=res_task)

