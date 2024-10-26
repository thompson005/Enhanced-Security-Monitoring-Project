import unittest
from src.analyzers.severity_analyzer import SeverityAnalyzer
from src.analyzers.trend_analyzer import TrendAnalyzer

class TestAnalyzers(unittest.TestCase):
    def setUp(self):
        self.cve_data = [
            {"id": "CVE-2021-1234", "cvss_score": 5.0, "published_date": "2021-01-01"},
            {"id": "CVE-2020-5678", "cvss_score": 9.0, "published_date": "2020-05-20"},
        ]
        self.severity_analyzer = SeverityAnalyzer()
        self.trend_analyzer = TrendAnalyzer()

    def test_severity_analysis(self):
        severity = self.severity_analyzer.analyze(self.cve_data)
        self.assertEqual(severity["CVE-2021-1234"], 5.0)
        self.assertEqual(severity["CVE-2020-5678"], 9.0)

    def test_trend_analysis(self):
        trends = self.trend_analyzer.analyze_trends(self.cve_data)
        self.assertEqual(trends['2021'], 1)
        self.assertEqual(trends['2020'], 1)

if __name__ == '__main__':
    unittest.main()
