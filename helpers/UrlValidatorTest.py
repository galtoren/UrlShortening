import unittest
from urllib.parse import urlparse
from url_validator import UrlValidator

class TestUrlValidator(unittest.TestCase):

    def setUp(self):
        self.validator = UrlValidator()

    def test_valid_url(self):
        valid_urls = [
            "https://www.example.com",
            "http://google.com",
        ]

        for url in valid_urls:
            self.assertTrue(self.validator.is_valid_url(url))

    def test_invalid_url(self):
        invalid_urls = [
            "invalid-url",
            "http://",
        ]

        for url in invalid_urls:
            self.assertFalse(self.validator.is_valid_url(url))

if __name__ == '__main__':
    unittest.main()
