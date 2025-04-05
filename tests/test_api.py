from fastapi.testclient import TestClient
from app.main import app
from app.repositories import ParameterRepository

client = TestClient(app)

def test_text_to_speech():
    response = client.post("/to_speech", json={"text": "Test text"})
    assert response.status_code == 200
    assert response.json() == {"status": "Speech played successfully"}

def test_text_to_speech_with_file():
    response = client.post(
        "/to_speech",
        json={"text": "Test text", "output_filename": "test.wav"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/wav"

def test_set_parameter():
    response = client.patch(
        "/set_parameter",
        json={"parameter_name": "rate", "parameter_value": "200"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "Parameter updated successfully"}

def test_get_parameters():
    response = client.get("/parameters")
    assert response.status_code == 200
    assert "rate" in response.json()