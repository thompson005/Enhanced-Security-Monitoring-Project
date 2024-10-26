from collections import Counter

class TrendAnalyzer:
    def analyze_trends(self, cve_data):
        year_count = Counter()
        for cve in cve_data:
            year = cve['published_date'].split('-')[0]
            year_count[year] += 1
        return year_count
