# src/run_collector.py

import os
import subprocess  # Import subprocess to run Logstash
from src.collectors.cve_collector import CVECollector
from src.collectors.exploit_db_collector import ExploitDBCollector
from src.collectors.github_security_collector import GithubSecurityCollector
from src.enrichment.cwe_enricher import CWEEnricher
from src.enrichment.threat_intel_enricher import ThreatIntelEnricher
from src.utils.logger import logger

def main():
    config_path = os.path.join("config", "collectors_config.yaml")

    # Initialize collectors
    cve_collector = CVECollector(config_path)
    exploit_db_collector = ExploitDBCollector(config_path)
    github_security_collector = GithubSecurityCollector(config_path)

    # Collect data
    cve_data = cve_collector.collect()
    exploit_data = exploit_db_collector.fetch_exploit_data()
    github_data = github_security_collector.fetch_github_data()

    # Initialize enrichers
    cwe_enricher = CWEEnricher()
    threat_intel_enricher = ThreatIntelEnricher()

    # Enrich CVE data
    enriched_cve_data = cwe_enricher.enrich(cve_data)
    fully_enriched_data = threat_intel_enricher.enrich(enriched_cve_data)

    # Save and send to Elasticsearch
    output_csv_path = os.path.join("data/raw", "cve_data.csv")
    cve_collector.save_to_csv(output_csv_path)

    # Run Logstash to process the CSV file and send to Elasticsearch
    logstash_command = [
        "logstash", "-f", "path/to/your/config/logstash.conf"  # Update to the path of your logstash.conf
    ]
    subprocess.run(logstash_command)

    logger.info("Data collection, enrichment, and Logstash processing completed.")

if __name__ == "__main__":
    main()
