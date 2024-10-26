# src/run_collector.py

import os
from src.collectors.cve_collector import CVECollector

def main():
    # Set up paths
    config_path = os.path.join("config", "collectors_config.yaml")
    collector = CVECollector(config_path)

    # Collect CVE data
    cve_data = collector.collect()

    # Save to CSV
    output_csv_path = os.path.join("data/raw", "cve_data.csv")
    collector.save_to_csv(output_csv_path)

if __name__ == "__main__":
    main()
