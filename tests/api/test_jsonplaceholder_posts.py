import requests

def test_get_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert r.status_code == 200

def test_create_post_and_get():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert r.status_code == 201
