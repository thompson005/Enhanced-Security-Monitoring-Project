import requests
import yaml
from src.utils.logger import logger

class GithubSecurityCollector:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.github_data = []

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def fetch_github_data(self):
        url = self.config['github_security_url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.github_data = response.json()
            logger.info("GitHub security data fetched successfully.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching GitHub security data: {e}")

    def get_github_data(self):
        return self.github_data
