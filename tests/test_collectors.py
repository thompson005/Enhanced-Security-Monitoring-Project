import unittest
from src.collectors.cve_collector import CVECollector
from src.collectors.exploit_db_collector import ExploitDBCollector
from src.collectors.github_security_collector import GithubSecurityCollector

class TestCVECollectors(unittest.TestCase):
    def test_cve_collector(self):
        collector = CVECollector('config/collectors_config.yaml')
        collector.fetch_cve_data()
        self.assertTrue(len(collector.get_cve_data()) > 0)

    def test_exploit_db_collector(self):
        collector = ExploitDBCollector('config/collectors_config.yaml')
        collector.fetch_exploit_data()
        self.assertTrue(len(collector.get_exploit_data()) > 0)

    def test_github_security_collector(self):
        collector = GithubSecurityCollector('config/collectors_config.yaml')
        collector.fetch_github_data()
        self.assertTrue(len(collector.get_github_data()) > 0)

if __name__ == '__main__':
    unittest.main()
