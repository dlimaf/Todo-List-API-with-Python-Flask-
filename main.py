from flask import Flask,request,jsonify

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route("/todos", methods=['POST','GET'])
def all_todos():
    if request.method == 'POST':
        tarea = request.get_json()
        todos.append(tarea)
        return todos
    elif request.method == 'GET':
        return jsonify(todos)

   
@app.route("/todos/<int:index>", methods=['DELETE'])
def delete_todos(index):
    todos.pop(index)
    return jsonify(todos)

app.run()