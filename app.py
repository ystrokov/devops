from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

@app.route('/api/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'GET':
        return jsonify([task.__dict__ for task in tasks])
    elif request.method == 'POST':
        data = request.json
        task = Task(data['title'], data['description'])
        tasks.append(task)
        return jsonify(task.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True)
