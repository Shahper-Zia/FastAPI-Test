import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_query_endpoint():
    response = client.post("/query", json={"question": "What is AI?"})
    assert response.status_code == 200
    assert "answer" in response.json()

def test_invalid_query():
    response = client.post("/query", json={"question": ""})
    assert response.status_code == 422  # Unprocessable Entity

def test_authentication():
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()