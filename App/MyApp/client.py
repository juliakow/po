import os
import requests
import logging

'''konfiguracja logowania'''
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(massage)s')

class IQAirClient:
    def __init__(self, api_key=None):
        self.base_url = "https://api.iqair.com/api"
        