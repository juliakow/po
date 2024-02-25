import pytest
from app import app
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code ==  200
    assert json.loads(response.data) == []

def test_create_user(client):
    response = client.post('/users', json={
        "id":  1,
        "firstName": "John",
        "lastName": "Doe",
        "birthYear":  1990,
        "group": "user"
    })
    assert response.status_code ==  201
    assert json.loads(response.data) == {
        "id":  1,
        "firstName": "John",
        "lastName": "Doe",
        "age":  32,
        "group": "user"
    }

def test_update_user(client):
    client.post('/users', json={
        "id":  1,
        "firstName": "John",
        "lastName": "Doe",
        "birthYear":  1990,
        "group": "user"
    })
    response = client.patch('/users/1', json={
        "firstName": "Jane"
    })
    assert response.status_code ==  200
    assert json.loads(response.data)["firstName"] == "Jane"

def test_delete_user(client):
    client.post('/users', json={
        "id":  1,
        "firstName": "John",
        "lastName": "Doe",
        "birthYear":  1990,
        "group": "user"
    })
    response = client.delete('/users/1')
    assert response.status_code ==  200
    assert json.loads(response.data) == {"message": "User deleted"}
