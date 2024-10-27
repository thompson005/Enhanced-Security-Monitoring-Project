
# Security Vulnerability Monitoring System

## Overview
The **Security Vulnerability Monitoring System** is an all-in-one solution designed to monitor, collect, analyze, and correlate vulnerability data from various sources in real time. The system aims to empower organizations and individuals with timely, actionable insights into vulnerabilities, enabling better risk management and response to security threats.

## Key Features
- **Real-Time CVE Monitoring**: Continuously fetches the latest Common Vulnerabilities and Exposures (CVEs) data, keeping you informed of new security threats.
- **Automated Severity Analysis**: Evaluates the severity of vulnerabilities with custom algorithms, assisting with prioritization based on risk level.
- **Trend Analysis**: Identifies trends in vulnerabilities, providing insights into the evolution of security threats over time.
- **Integrated Data Sources**: Collects data from multiple reputable sources, including CVE databases, Exploit-DB, and GitHub Security Advisories, ensuring a comprehensive view of potential threats.
- **Elastic Stack Visualization**: Employs Elasticsearch and Kibana to visualize and monitor vulnerability data for an intuitive and actionable overview.
- **Automated Alerting**: Notifies users of critical vulnerabilities in real time, helping with rapid response and mitigation.

## Architecture
The system follows a modular architecture composed of distinct components, each responsible for specific functionality:

- **Data Collectors**: Retrieve vulnerability data from sources like CVE databases, Exploit-DB, and GitHub Security Advisories.
- **Data Enrichment**: Enhances data with contextual information, e.g., adding CWE (Common Weakness Enumeration) details or threat intelligence.
- **Data Analysis**: Analyzes vulnerability severity and trends over time, detecting correlation patterns among different data points.
- **Data Storage**: Stores the data in Elasticsearch for fast retrieval and analysis.
- **Data Visualization**: Uses Kibana for dashboards and reporting, enabling users to view and interpret vulnerability insights.

## Technology Stack
- **Backend**: Python
- **Data Storage and Search**: Elasticsearch
- **Data Collection**: requests library for API interactions
- **Logging**: Custom logging utility for improved traceability
- **Containerization**: Docker and Docker Compose to simplify setup and deployment
- **Testing**: Pytest for automated testing and quality assurance

## Installation Guide

### Prerequisites
Ensure the following are installed:
- Python 3.7 or higher
- Docker and Docker Compose (for deploying Elasticsearch and Kibana)
- pip (Python package manager)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/thompson005/Enhanced-Security-Monitoring-Project.git
   cd Enhanced-Security-Monitoring-Project
   ```

2. **Install Dependencies**  
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Collectors**  
   Copy the example configuration file, then edit it with your settings:
   ```bash
   cp config/collectors_config.yaml.example config/collectors_config.yaml
   ```

4. **Start the Elastic Stack**  
   Navigate to the config directory and start the ELK stack with Docker Compose:
   ```bash
   cd config
   docker-compose up -d
   ```

5. **Run the Data Collector**  
   Begin collecting CVE data with the CVE collector:
   ```bash
   python -m src.collectors.cve_collector
   ```

## Directory Structure
The project's directory layout follows a modular structure for improved organization:

```plaintext
cve_monitoring_system/
├── src/
│   ├── collectors/                  # Data collection modules (e.g., CVE, Exploit-DB)
│   ├── analyzers/                   # Analysis modules (e.g., severity, trends)
│   ├── enrichment/                  # Enrichment modules for adding extra context
│   └── utils/                       # Utilities (e.g., config, logger)
├── config/                          # Configuration files for ELK and collectors
├── tests/                           # Unit tests for the system components
├── data/                            # Storage for raw and processed data
├── docs/                            # Documentation files (e.g., setup, architecture)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## System API Endpoints (Planned)
Note: Flask API management is under development and will be added in future updates.

## Running Tests
To verify the functionality, run the test suite:
```bash
python -m pytest tests/
```

## Contributing
We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and open a pull request.
