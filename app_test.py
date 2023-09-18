import requests
import unittest
import random
import string


class AppTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://0.0.0.0:8000"

    def test_generate_shorter_url(self):
        url = f"{self.base_url}/generate_shorter_url"
        data = {
            "url": generate_random_string(100),
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_generate_shorter_url_already_exist(self):
        url = f"{self.base_url}/generate_shorter_url"
        random_url_to_short = generate_random_string(100)
        data = {
            "url": random_url_to_short,
        }
        first_response = requests.post(url, json=data)
        second_response = requests.post(url, json=data)
        self.assertEqual(first_response.status_code, 200)
        self.assertEqual(second_response.status_code, 409)

    def test_get_origin_url(self):
        generate_url = f"{self.base_url}/generate_shorter_url"
        data = {
            "url": generate_random_string(100),
        }
        post_response = requests.post(generate_url, json=data)
        get_url = f"{self.base_url}/get_origin_url"
        generated_url = post_response.json()  # This will convert the JSON response to a Python dictionary
        get_response = requests.get(url=f"{get_url}",
                                    params={'url': generated_url['shorter_url']})
        self.assertEqual(get_response.status_code, 200)

    def test_url_not_found(self):
        get_url = f"{self.base_url}/get_origin_url"
        url = "https://gat_toren/nice_url_mate"
        response = requests.get(url=f"{get_url}",
                                params={'url': url})
        self.assertEqual(response.status_code, 404)


def generate_random_string(length: int):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
