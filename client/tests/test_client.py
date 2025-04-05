import unittest
import pytest
from unittest.mock import patch, MagicMock
from client import OratorClient
from models import ClientConfig

@pytest.fixture
def client():
    config = ClientConfig(server_url="http://testserver")
    return OratorClient(config)

def test_text_to_speech(client):
    with patch('requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        client.text_to_speech("Test text")
        mock_post.assert_called_once_with(
            "http://testserver/to_speech",
            json={"text": "Test text"}
        )

def test_text_to_speech_with_file(client):
    with patch('requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'test_audio'
        mock_post.return_value = mock_response
        
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            client.text_to_speech("Test text", "test.wav")
            
            mock_post.assert_called_once_with(
                "http://testserver/to_speech",
                json={"text": "Test text", "output_filename": "test.wav"}
            )
            mock_file.assert_called_once_with("test.wav", 'wb')

def test_set_parameter(client):
    with patch('requests.patch') as mock_patch:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_patch.return_value = mock_response
        
        client.set_parameter("rate", "200")
        mock_patch.assert_called_once_with(
            "http://testserver/set_parameter",
            json={"parameter_name": "rate", "parameter_value": "200"}
        )

def test_text_file_to_speech(client):
    with patch('builtins.open', unittest.mock.mock_open(read_data="file content")) as mock_file:
        with patch.object(client, 'text_to_speech') as mock_text_to_speech:
            client.text_file_to_speech("input.txt", "output.wav")
            
            mock_file.assert_called_once_with("input.txt", 'r')
            mock_text_to_speech.assert_called_once_with("file content", "output.wav")