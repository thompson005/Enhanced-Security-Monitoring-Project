Security Vulnerability Monitoring and Analysis System - Setup Guide
Prerequisites

Python 3.9 or higher
Docker and Docker Compose
Elasticsearch, Logstash, and Kibana (provided by Docker Compose)

Installation

Clone the repository:
Copygit clone https://github.com/your-username/security-monitoring-system.git

Create a virtual environment and activate it:
Copypython -m venv venv
source venv/bin/activate

Install the required dependencies:
Copypip install -r requirements.txt

Configure the environment:

Copy the example configuration file:
Copycp config/collectors_config.yaml.example config/collectors_config.yaml

Edit the config/collectors_config.yaml file and update the settings according to your requirements.
Set the necessary environment variables (e.g., GITHUB_TOKEN, VIRUSTOTAL_API_KEY, ALIENVAULT_API_KEY).


Start the Elastic Stack:
Copydocker-compose up -d

Run the data collectors:
Copypython -m src.collectors.cve_collector
python -m src.collectors.exploit_db_collector
python -m src.collectors.github_security_collector

Verify the data in Kibana:

Open your web browser and navigate to http://localhost:5601.
Explore the security data in the Kibana dashboards.



Usage

The src/collectors directory contains the scripts responsible for fetching and processing data from various sources.
The src/enrichment directory includes the modules that enhance the collected data with additional context and intelligence.
The src/analyzers directory holds the components responsible for analyzing the security data, such as the severity analyzer, trend analyzer, and correlation engine.
The src/utils directory contains utility modules, including the configuration loader, logger, and other shared functions.
The config directory stores the configuration files for the different components of the system.
The data directory is used to store the collected and processed security data.
The docs directory can be used to store any relevant documentation, setup guides, and architectural diagrams.

Feel free to explore the codebase, modify the configurations, and implement additional features as per your requirements.
