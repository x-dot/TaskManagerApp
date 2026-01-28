import json
import os
from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)
DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = load_tasks()
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task:
        return jsonify(task), 200
    return abort(404, description="Task not found")

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400, description="Bad Request: Title is required")
    
    tasks = load_tasks()
    
    # generates new id (max id + 1)
    if tasks:
        new_id = max(task['id'] for task in tasks) + 1
    else:
        new_id = 1
        
    new_task = {
        'id': new_id,
        'username': request.json.get('username', ''),
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'deadline': request.json.get('deadline', '')
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    task = next((item for item in tasks if item["id"] == task_id), None)
    
    if not task:
        abort(404, description="Task not found")
        
    tasks.remove(task)
    save_tasks(tasks)
    return jsonify({'result': True}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')