from .repositories import ParameterRepository
from .services import SpeechService

def get_parameter_repository() -> ParameterRepository:
    return ParameterRepository()

def get_speech_service() -> SpeechService:
    param_repo = get_parameter_repository()
    return SpeechService(param_repo)