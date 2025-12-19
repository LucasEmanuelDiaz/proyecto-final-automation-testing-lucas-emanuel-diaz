import requests

BASE = "https://dummyjson.com"

HEADERS = {
    "User-Agent": "pytest-api-tests",
    "Content-Type": "application/json"
}

def test_get_users_list():
    r = requests.get(f"{BASE}/users?limit=10", headers=HEADERS)

    # ✅ GET → 200
    assert r.status_code == 200

    data = r.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0


def test_post_create_user():
    payload = {
        "firstName": "Morpheus",
        "lastName": "QA",
        "age": 35
    }

    r = requests.post(
        f"{BASE}/users/add",
        json=payload,
        headers=HEADERS
    )

    # ✅ POST → 201
    assert r.status_code == 201

    data = r.json()
    assert data.get("firstName") == payload["firstName"]
    assert "id" in data


def test_delete_user():
    r = requests.delete(f"{BASE}/users/1", headers=HEADERS)

    # ✅ DELETE → 200
    assert r.status_code == 200

    data = r.json()
    assert data.get("isDeleted") is True
