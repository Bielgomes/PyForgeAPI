from pytest import fixture
from pytest import mark
from httpx import AsyncClient

from fastipy import TestClient

from .api import app, reset


@fixture
def client():
    return TestClient(app)


def test_get(client):
    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": []}


def test_create_messages(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})
    assert response.status_code == 201


def test_get_messages(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})
    assert response.status_code == 201

    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": ["Hello, World!"]}


def test_delete_messages(client):
    reset()

    response = client.post("/messages", json={"message": "Hello, World!"})
    assert response.status_code == 201

    response = client.delete("/messages")
    assert response.status_code == 204

    response = client.get("/messages")
    assert response.json() == {"messages": []}


def test_get_empty_messages(client):
    reset()

    response = client.get("/messages")
    assert response.status_code == 200
    assert response.json() == {"messages": []}


def test_route_params(client):
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_route_params_with_scapes(client):
    response = client.get("/hello/John%2fWillian")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John%2fWillian!"}


def test_route_query_params(client):
    response = client.get("/hello?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}


def test_plain_text_response(client):
    response = client.get("/plain-text")
    assert response.status_code == 200
    assert response.text == "Hello, World!"


def test_html_response(client):
    response = client.get("/html")
    assert response.status_code == 200
    assert response.text == "<h1>Hello, World!</h1>"
    assert response.headers["Content-Type"] == "text/html"


@mark.asyncio
async def test_stream_response(client):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/stream")
        assert response.status_code == 200
        assert response.text == "Hello, World!"


def test_route_not_found(client):
    response = client.get("/not-found")
    assert response.status_code == 404
