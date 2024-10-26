class SeverityAnalyzer:
    def analyze(self, cve_data):
        severity = {}
        for cve in cve_data:
            score = cve.get('cvss_score', 0)
            severity[cve['id']] = score
        return severity
