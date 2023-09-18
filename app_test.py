import requests
import unittest


class AppTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://0.0.0.0:8000"

    def test_generate_shorter_url(self):
        url = f"{self.base_url}/generate_shorter_short"
        data = {
            "url": "http:",
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_origin_url(self):
        generate_url = f"{self.base_url}/generate_shorter_short"
        data = {
            "url": "http:",  # TODO: add a long url here and check the logic after implemented
        }
        response = requests.post(generate_url, json=data)
        get_url = f"{self.base_url}/get_origin_url"
        generated_url = response.json()  # This will convert the JSON response to a Python dictionary
        response = requests.get(url=f"{get_url}",
                                params={'url': generated_url['id']})
        self.assertEqual(response.status_code, 200)

    def test_url_not_found(self):
        get_url = f"{self.base_url}/get_origin_url"
        url = "https://chat.openai.com/"
        response = requests.get(url=f"{get_url}",
                                params={'url': url})
        self.assertEqual(response.status_code, 404)
