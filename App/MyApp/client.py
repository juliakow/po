import os
import requests
import logging

'''konfiguracja logowania'''
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(massage)s')

class IQAirClient:
    def __init__(self, api_key=None):
        self.base_url = "https://api.iqair.com/api"
        self.api_key = api_key or os.getenv("IQAIR_API_KEY")
        if not self.api_key:
            raise ValueError("API key is not set. Please set IQAIR_API_KEY environment variable or pass it as an argument.")
        self.logger = logging.getLogger(__name__)

    def get_air_quality_data(self, city="Warszawa"):
        try:
            response = requests.get(
                f"{self.base_url}/v2/air/quality",
                params={"city": city},
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching air quality data: {e}")
            return None
        