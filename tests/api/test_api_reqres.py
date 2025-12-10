import requests

BASE = 'https://reqres.in/api'

def test_get_users_list():
    r = requests.get(f"{BASE}/users?page=2")
    assert r.status_code == 200
    data = r.json()
    assert 'data' in data
    assert isinstance(data['data'], list)

def test_post_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{BASE}/users", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data.get('name') == payload['name']
    assert 'id' in data

def test_delete_user():
    r = requests.delete(f"{BASE}/users/2")
    assert r.status_code in (204, 200, 202)
