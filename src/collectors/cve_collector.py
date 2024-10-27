import requests
import json
from kafka import KafkaProducer
import logging
import yaml

logger = logging.getLogger(__name__)

class CVECollector:
    def __init__(self, config_path, kafka_topic):
        self.config = self.load_config(config_path)
        self.cve_data = []
        self.kafka_topic = kafka_topic
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',  # Adjust if your Kafka server is different
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

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

    def send_to_kafka(self):
        try:
            for data in self.cve_data:
                self.producer.send(self.kafka_topic, data)
            logger.info("CVE data sent to Kafka successfully.")
        except Exception as e:
            logger.error(f"Error sending data to Kafka: {e}")

    def collect(self):
        self.fetch_cve_data()
        self.send_to_kafka()
