from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@149.154.66.32:5432/mydatabase'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'GET':
        tasks = Task.query.all()
        task_list = []
        for task in tasks:
            task_list.append({
                'id': task.id,
                'task': task.task,
                'description': task.description
            })
        return jsonify(task_list)

    elif request.method == 'POST':
        data = request.json
        new_task = Task(task=data['task'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully', 'id': new_task.id}), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
