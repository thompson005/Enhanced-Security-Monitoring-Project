import requests
from src.utils.logger import logger

class ThreatIntelEnricher:
    def __init__(self):
        self.threat_intel_api_url = "https://threat-intel-api.com/threats/"  # Placeholder URL

    def enrich(self, cve_data):
        enriched_data = []
        for cve in cve_data:
            threat_intel = self.fetch_threat_intel(cve['id'])
            enriched_data.append({**cve, 'threat_intel': threat_intel})
        return enriched_data

    def fetch_threat_intel(self, cve_id):
        """Fetch threat intelligence data based on CVE ID."""
        url = f"{self.threat_intel_api_url}{cve_id}"  # Build URL for specific CVE
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()  # Assuming the response is JSON
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching threat intelligence for CVE ID {cve_id}: {e}")
            return "Threat intelligence data not available"
