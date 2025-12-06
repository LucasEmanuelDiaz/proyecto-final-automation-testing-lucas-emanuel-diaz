import requests

def test_get_users():
    r = requests.get('https://reqres.in/api/users?page=2')
    assert r.status_code == 200

def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post('https://reqres.in/api/users', json=payload)
    assert r.status_code == 201

def test_delete_user():
    r = requests.delete('https://reqres.in/api/users/2')
    assert r.status_code in (204, 200)
