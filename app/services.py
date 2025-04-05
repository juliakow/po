import pyttsx3
import os
from pathlib import Path
from typing import Optional

class SpeechService:
    def __init__(self, parameter_repository):
        self.parameter_repository = parameter_repository

    def text_to_speech(self, text: str, output_file: Optional[str] = None) -> bytes:
        engine = pyttsx3.init()
        
        params = self.parameter_repository.get_all_parameters()
        engine.setProperty('rate', int(params['rate']))
        engine.setProperty('volume', float(params['volume']))
        
        voices = engine.getProperty('voices')
        voice_index = int(params['voice'])
        if 0 <= voice_index < len(voices):
            engine.setProperty('voice', voices[voice_index].id)
        
        if output_file:
            temp_file = "temp.wav"
            engine.save_to_file(text, temp_file)
            engine.runAndWait()
            
            with open(temp_file, 'rb') as f:
                content = f.read()
            
            os.remove(temp_file)
            return content
        else:
            engine.say(text)
            engine.runAndWait()
            return b''