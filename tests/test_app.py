import pytest
import json
import os
import sys

# psaxnei to app.py pou einai ston apo panw fakelo.. gt to ekana auto??
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    # fake file gia test 
    app.config['TESTING'] = True
    
    # ena temp file
    import app as app_module
    original_db = app_module.DATA_FILE
    app_module.DATA_FILE = 'test_tasks_temp.json'
    
    # anoigw client gia to test
    with app.test_client() as client:
        yield client
        
    # svhnw to tempfile meta to test
    if os.path.exists('test_tasks_temp.json'):
        os.remove('test_tasks_temp.json')
    
    # kai fernw to kanoniko file
    app_module.DATA_FILE = original_db
    
    # elegxei an einai kenh h lista
def test_get_tasks_empty(client):
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert json.loads(rv.data) == []


    #elegxei an mporw na kanw new task
def test_create_task(client):
    new_task = {
        "username": "test_user",
        "title": "Unit Test Task",
        "description": "Checking if creating works",
        "deadline": "2027-01-01"
    }
    rv = client.post('/tasks', json=new_task)
    assert rv.status_code == 201
    data = json.loads(rv.data)
    assert data['title'] == "Unit Test Task"
    assert data['id'] == 1

    #elegxei th diagrafh
def test_delete_task(client):
    # 1. ftiaxnei task
    client.post('/tasks', json={"title": "To Be Deleted"})
    
    # 2. to diagrafei (id 1)
    rv = client.delete('/tasks/1')
    assert rv.status_code == 200
    
    # 3. elegxei an ontws ekane delete (prepei na doume error 404)
    rv_check = client.get('/tasks/1')
    assert rv_check.status_code == 404
    
