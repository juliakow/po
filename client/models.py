from typing import Optional

class ClientConfig:
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url