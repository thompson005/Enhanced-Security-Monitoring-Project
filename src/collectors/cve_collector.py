import requests
import yaml
import pandas as pd
from elasticsearch import Elasticsearch
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
            response.raise_for_status()  # Checks for HTTP errors
            logger.info(f"Response Status Code: {response.status_code}")
            self.cve_data = response.json()  # Load JSON data directly
            if isinstance(self.cve_data, list):
                logger.info("CVE data fetched successfully.")
            else:
                logger.warning("Unexpected data format. No CVE data found.")
                self.cve_data = []
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

    def send_to_elasticsearch(self):
        """Send collected CVE data to Elasticsearch."""
        if not self.cve_data:
            logger.warning("No CVE data to send to Elasticsearch.")
            return

        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        for entry in self.cve_data:
            try:
                res = es.index(index="cve-index", document=entry)
                logger.info(f"Data indexed in Elasticsearch: {res['result']}")
            except Exception as e:
                logger.error(f"Error sending data to Elasticsearch: {e}")

# Example usage
if __name__ == "__main__":
    collector = CVECollector("config/collectors_config.yaml")
    collector.collect()
    collector.save_to_csv("output/cve_data.csv")
    collector.send_to_elasticsearch()
