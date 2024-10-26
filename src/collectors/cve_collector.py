import requests
import yaml
import pandas as pd
import os
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
            self.cve_data = response.json()
            logger.info("CVE data fetched successfully.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching CVE data: {e}")
            self.cve_data = []  # Clear data on error

    def get_cve_data(self):
        return self.cve_data

    def collect(self):
        """Collect CVE data from the source and return it."""
        self.fetch_cve_data()
        return self.get_cve_data()

    def save_to_csv(self, output_path):
        """Save collected CVE data to a CSV file."""
        if not self.cve_data:
            logger.warning("No CVE data to save.")
            return

        df = pd.DataFrame(self.cve_data)
        df.to_csv(output_path, index=False)
        logger.info(f"CVE data saved to {output_path}")
