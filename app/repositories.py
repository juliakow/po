from typing import Dict

class ParameterRepository:
    def __init__(self):
        self._parameters: Dict[str, str] = {
            'rate': '150',   
            'volume': '1.0', 
            'voice': '0'      
        }

    def get_parameter(self, name: str) -> str:
        return self._parameters.get(name, '')

    def set_parameter(self, name: str, value: str) -> None:
        if name in self._parameters:
            self._parameters[name] = value

    def get_all_parameters(self) -> Dict[str, str]:
        return self._parameters.copy()