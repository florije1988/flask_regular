# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, render_template
from flask.ext.restful import Resource, Api

app = Flask(__name__)
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
api = Api(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
