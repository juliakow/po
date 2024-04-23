import os 
import requests


# jest to klasa ktora umozliwia pobieranie danych
class AirQualityClient:
    def __init__(self, station_id = None):
        self.api_key = os.getenv('AIR_QUALITY_API_KEY')
        self.station_id = station_id or os.getenv('AIR_QUALITY_STATION_ID')
        self.base_url = "https://api-docs.iqair.com/"

    def get_air_quality_data(self):
        params = {
            'station_id': self.station_id,
            'api_key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else: 
            raise Exception(f"Failed to fetch data: {response.text}")
        
if __name__ == "__main__":
    client = AirQualityClient()
    data = client.get_air_quality_data()
    print(data)