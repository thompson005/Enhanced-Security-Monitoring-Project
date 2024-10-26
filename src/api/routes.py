from flask import jsonify, request
from src.collectors.cve_collector import CVECollector  # Import the CVECollector class
from src.analyzers.severity_analyzer import analyze_severity  # Ensure this function is defined
from src.api import app  # Import the Flask app instance
import os

# Initialize CVE Collector
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'collectors_config.yaml')
cve_collector = CVECollector(config_path)

@app.route('/api/collect', methods=['POST'])
def collect():
    """
    Collect CVEs from sources.
    """
    try:
        result = cve_collector.collect()  # Use the collector's method to collect CVEs
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyze the severity of collected CVEs.
    """
    data = request.json
    if 'cves' not in data:
        return jsonify({"error": "No CVEs provided"}), 400
    
    try:
        result = analyze_severity(data['cves'])  # Call the function to analyze severity
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/status', methods=['GET'])
def status():
    """
    Check the status of the monitoring system.
    """
    return jsonify({"status": "running"}), 200
