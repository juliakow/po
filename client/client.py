import requests
from typing import Optional
from pathlib import Path
from .models import ClientConfig

class OratorClient:
    def __init__(self, config: ClientConfig):
        self.config = config

    def text_to_speech(self, text: str, output_file: Optional[str] = None) -> None:
        url = f"{self.config.server_url}/to_speech"
        data = {"text": text}
        
        if output_file:
            data["output_filename"] = output_file
        
        response = requests.post(url, json=data)
        
        if response.status_code != 200:
            raise Exception(f"Server error: {response.text}")
        
        if output_file:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"Speech saved to {output_file}")
        else:
            print("Speech played successfully")

    def set_parameter(self, parameter_name: str, parameter_value: str) -> None:
        url = f"{self.config.server_url}/set_parameter"
        data = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value
        }
        
        response = requests.patch(url, json=data)
        
        if response.status_code != 200:
            raise Exception(f"Server error: {response.text}")
        
        print(f"Parameter {parameter_name} set to {parameter_value}")

    def text_file_to_speech(self, input_file: str, output_file: Optional[str] = None) -> None:
        with open(input_file, 'r') as f:
            text = f.read()
        
        self.text_to_speech(text, output_file)