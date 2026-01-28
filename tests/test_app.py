import pytest
import json
import os
import app as app_module  # Κάνουμε import το app.py
from app import app

@pytest.fixture
def client():
    # Ρύθμιση για testing
    app.config['TESTING'] = True
    
    # Χρήση temp για το temp.jason
    original_db = app_module.DATA_FILE
    app_module.DATA_FILE = 'test_tasks_temp.json'
    
    # delete ama uparxei
    if os.path.exists(app_module.DATA_FILE):
        os.remove(app_module.DATA_FILE)

    with app.test_client() as client:
        yield client

    # teardown
    if os.path.exists(app_module.DATA_FILE):
        os.remove(app_module.DATA_FILE)
    app_module.DATA_FILE = original_db

def test_create_task(client):
    """elegxei an dhmiourghthhke task"""
    new_task = {"title": "Test Task", "deadline": "2025-01-01"}
    response = client.post('/tasks', json=new_task)
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == "Test Task"
    assert data['id'] == 1

def test_get_all_tasks(client):
    """elegxei an epistrefei lista me tasks"""
    # ftiaxnoyme ena task
    client.post('/tasks', json={"title": "Task 1"})
    
    response = client.get('/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

def test_get_task_by_id(client):
    """elegxei an pairnoume sudkekrimeno id"""
    client.post('/tasks', json={"title": "Find Me"})
    
    #anazhthsh tou id 1
    response = client.get('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == "Find Me"
    assert data['id'] == 1

def test_get_task_not_found(client):
    """Ελέγχει αν παίρνουμε 404 για ανύπαρκτο ID"""
    response = client.get('/tasks/999')
    assert response.status_code == 404

def test_delete_task(client):
    """Ελέγχει τη διαγραφή"""
    client.post('/tasks', json={"title": "Delete Me"})
    
    # delete task 1
    response = client.delete('/tasks/1')
    assert response.status_code == 200
    
    # sigoureuei oti diagrafthke kai episrtefei 404 an oxi 
    response_check = client.get('/tasks/1')
    assert response_check.status_code == 404