from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get')
def get_tasks():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append({"id": task.id, "name": task.name, "description": task.description })
    return result


@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    name = data['name']
    description = data['description']

    if name:
        new_task = Task(name=name, description=description)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.get_json()
    name = data['name']
    description = data['description']

    task_to_update = db.session.get(Task, task_id)  # Zalóżmy, że rekord z ID 1 istnieje
    if task_to_update:
        task_to_update.name = name
        task_to_update.description = description
        db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')