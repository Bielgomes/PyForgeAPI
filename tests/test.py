from pytest import fixture

from fastify import TestClient

from .api import app, reset


@fixture
def client():
    return TestClient(app)


def test_get(client):
    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": []}


def test_post(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})
    assert response.status_code == 201


def test_get_messages(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})

    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": ["Hello, World!"]}


def test_delete_messages(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})

    response = client.delete("/messages")
    assert response.status_code == 204

    response = client.get("/messages")
    assert response.json() == {"messages": []}


def test_get_messages_empty(client):
    reset()

    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": []}


def test_hello_name(client):
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_hello_name_query(client):
    response = client.get("/hello?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_route_not_found(client):
    response = client.get("/not-found")
    assert response.status_code == 404
