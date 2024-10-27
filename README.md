# Security Vulnerability Monitoring System

## Overview
The **Security Vulnerability Monitoring System** is a real-time tool that tracks, analyzes, and visualizes vulnerability data from various sources, using the ELK stack for powerful security threat management.

## Key Features
- **Real-Time Monitoring**: Live vulnerability data updates
- **Severity Analysis**: Automated vulnerability prioritization
- **Trend Visualization**: Security trend insights
- **Multi-Source Integration**: Combined data from multiple sources
- **Custom Dashboards**: Easy-to-use Kibana dashboards

  
## Technology Stack
- **Backend**: Python
- **Storage**: Elasticsearch
- **Collection**: requests library
- **Container**: Docker & Docker Compose
- **Testing**: Pytest

## Quick Setup

1. **Install & Configure**
   ```bash
   git clone https://github.com/thompson005/Enhanced-Security-Monitoring-Project.git
   cd Enhanced-Security-Monitoring-Project
   pip install -r requirements.txt
   ```

2. **Start ELK Stack**
   ```bash
   cd config
   docker-compose up -d
   ```

3. **Launch Collector**
   ```bash
   python -m src.collectors.cve_collector
   ```

4. **View Dashboard**
   ```
   URL: http://localhost:5601
   Username: elastic
   Password: changeme
   ```

## Architecture

Collectors -> Enrichment -> Analysis -> Storage -> Visualization
   │             │            │           │            │
   └─ CVE        └─ CWE       └─ Severity └─ Elasticsearch └─ Kibana
   │             │            │           │            │
   └─ ExploitDB  └─ ThreatInt └─ Trends   └─ JSON      └─ Dashboards
   │                                      │            
   └─ GitHub Sec                          └─ Indexing     
   │                                                  
   └─ API Calls                                       

## Status

### Available Now
- ✅ CVE Collection
- ✅ ELK Integration
- ✅ Dashboards

### Coming Soon
- 🚧 Web Interface
- 🚧 Advanced Alerts

## Structure
```
project/
├── src/        # Core code
├── config/     # Settings
├── tests/      # Testing
└── data/       # Storage
```

## Contributing
Fork the repo, make your changes, and submit a pull request!

## License
MIT
