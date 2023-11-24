print("hello")

from flask import Flask, request # app.py, app2.py와 달리 request를 import해줌
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}
count = 1

@api.route('/todos')
class TodoPost(Resource):
    def post(self):
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {
            'todo_id': idx,
            'data': todos[idx]
        }


@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def delete(self, todo_id):
        del todos[todo_id]
        return {
            "delete": "success"
        }


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)

