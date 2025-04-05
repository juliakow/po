from pydantic import BaseModel
from typing import Optional

class SpeechRequest(BaseModel):
    text: str
    output_filename: Optional[str] = None

class ParameterUpdate(BaseModel):
    parameter_name: str
    parameter_value: str