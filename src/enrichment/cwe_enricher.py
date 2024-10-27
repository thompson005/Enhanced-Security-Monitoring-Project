import requests
from src.utils.logger import logger

class CWEEnricher:
    def __init__(self):
        self.cwe_api_url = "https://cwe.mitre.org/data/definitions/"  # CWE definitions URL

    def enrich(self, cve_data):
        enriched_data = []
        for cve in cve_data:
            cwe_id = cve.get('cwe_id', 'N/A')
            if cwe_id != 'N/A':
                cwe_description = self.fetch_cwe_description(cwe_id)
                enriched_data.append({**cve, 'cwe_description': cwe_description})
            else:
                enriched_data.append(cve)
        return enriched_data

    def fetch_cwe_description(self, cwe_id):
        """Fetch the CWE description based on the ID."""
        url = f"{self.cwe_api_url}{cwe_id}.html"  # Build URL for specific CWE
        try:
            response = requests.get(url)
            response.raise_for_status()
            # Extract the CWE description from the HTML page (Placeholder, needs actual parsing)
            return f"Description for CWE {cwe_id}"  # Placeholder implementation
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching CWE description for ID {cwe_id}: {e}")
            return "CWE description not available"
