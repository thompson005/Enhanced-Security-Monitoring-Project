import requests
import yaml
import os
from dotenv import load_dotenv
from src.utils.logger import logger

# Load environment variables from .env file
load_dotenv()

class GithubSecurityCollector:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.github_data = []
        self.github_token = os.getenv('GITHUB_TOKEN')  # Load from environment variable

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def fetch_github_data(self):
        url = self.config['github_security_url']
        headers = {
            'Authorization': f'token {self.github_token}'  # Use the token in the headers
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            self.github_data = response.json()
            logger.info("GitHub security data fetched successfully.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching GitHub security data: {e}")

    def get_github_data(self):
        return self.github_data
