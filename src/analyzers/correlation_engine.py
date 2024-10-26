class CorrelationEngine:
    def correlate_data(self, cve_data, exploit_data):
        correlated = []
        for cve in cve_data:
            for exploit in exploit_data:
                if cve['id'] == exploit['cve_id']:
                    correlated.append({
                        'cve': cve,
                        'exploit': exploit
                    })
        return correlated
