import logging
from collectors.cve_collector import CVECollector
from collectors.github_security_collector import GithubSecurityCollector

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def main():
    # Paths to configuration files
    cve_config_path = 'config/cve_config.yaml'
    github_config_path = 'config/github_config.yaml'
    kafka_topic = 'cve_data'  # Your Kafka topic name

    # Initialize the CVE Collector
    cve_collector = CVECollector(cve_config_path, kafka_topic)
    # Initialize the GitHub Security Collector
    github_collector = GithubSecurityCollector(github_config_path)

    # Collect CVE data and send it to Kafka
    cve_collector.collect()
    # Collect GitHub security advisory data
    github_collector.collect()  

if __name__ == "__main__":
    main()
