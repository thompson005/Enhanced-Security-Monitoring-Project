
# Security Vulnerability Monitoring and Analysis System - Setup Guide

## Prerequisites

Ensure the following are installed and configured before proceeding:
- **Python**: Version 3.9 or higher
- **Docker** and **Docker Compose**
- **Elasticsearch**, **Logstash**, and **Kibana** (provided via Docker Compose)

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/security-monitoring-system.git
```

### Step 2: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Environment
1. Copy the example configuration file:
    ```bash
    cp config/collectors_config.yaml.example config/collectors_config.yaml
    ```
2. Edit `config/collectors_config.yaml` to update the settings based on your requirements.
3. Set the necessary environment variables:
    - `GITHUB_TOKEN`
    - `VIRUSTOTAL_API_KEY`
    - `ALIENVAULT_API_KEY`

---

## Running the System

### Step 1: Start the Elastic Stack
```bash
docker-compose up -d
```

### Step 2: Run the Data Collectors
```bash
python -m src.collectors.cve_collector
python -m src.collectors.exploit_db_collector
python -m src.collectors.github_security_collector
```

---

## Verification

1. Open your browser and navigate to [http://localhost:5601](http://localhost:5601).
2. Explore the security data in the **Kibana dashboards**.

---

## Codebase Overview

- **`src/collectors`**: Contains scripts to fetch and process data from various sources.
- **`src/enrichment`**: Includes modules for enhancing data with additional context and intelligence.
- **`src/analyzers`**: Holds components for analyzing security data (e.g., severity analyzer, trend analyzer, correlation engine).
- **`src/utils`**: Utility modules like configuration loader, logger, and shared functions.
- **`config`**: Stores configuration files for system components.
- **`data`**: Used for storing collected and processed security data.
- **`docs`**: Contains relevant documentation, setup guides, and architectural diagrams.

---

## Customization

Feel free to explore the codebase, modify configurations, and implement additional features as needed.

---

## License

This project is licensed under the [MIT License](LICENSE).
