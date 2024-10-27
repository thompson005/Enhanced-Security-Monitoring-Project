import requests
import yaml
from src.utils.logger import logger

class CVECollector:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.cve_data = []

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def fetch_cve_data(self):
        url = self.config['cve_api_url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.cve_data = response.json().get('CVE_Items', [])
            logger.info("CVE data fetched successfully.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching CVE data: {e}")

    def collect(self):
        self.fetch_cve_data()
        return self.cve_data

    def send_to_logstash(self, cve_data):
        logstash_url = "http://localhost:5044"  # Replace with your Logstash URL if different
        try:
            response = requests.post(logstash_url, json=cve_data)
            response.raise_for_status()  # Raise an error for bad responses
            logger.info("CVE data sent to Logstash successfully.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending data to Logstash: {e}")

    def save_to_csv(self, output_csv_path):
        import pandas as pd

        df = pd.DataFrame(self.cve_data)
        df.to_csv(output_csv_path, index=False)
        logger.info(f"CVE data saved to {output_csv_path}.")
