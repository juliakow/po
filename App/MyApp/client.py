import os
import requests
import logging

'''konfiguracja logowania'''
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(massage)s')