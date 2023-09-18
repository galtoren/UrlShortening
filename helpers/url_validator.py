from urllib.parse import urlparse


class UrlValidator:

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme != '', result.netloc != ''])
        except ValueError:
            return False
