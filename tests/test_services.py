import sys
from pathlib import Path
import pytest
from app.repositories import ParameterRepository
from app.services import SpeechService

sys.path.append(str(Path('C:\\Users\\julia\\OneDrive\\Pulpit\\vsc\\2023-2024\\po\\server')))

@pytest.fixture
def param_repo():
    return ParameterRepository()

@pytest.fixture
def speech_service(param_repo):
    return SpeechService(param_repo)

def test_text_to_speech(speech_service):
    result = speech_service.text_to_speech("test")
    assert result == b''

def test_text_to_speech_with_file(speech_service):
    result = speech_service.text_to_speech("test", "test.wav")
    assert isinstance(result, bytes)
    assert len(result) > 0