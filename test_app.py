import unittest
from app import translate_it, URL, API_KEY
import requests


class MyTestCase(unittest.TestCase):
    def test_translate_it_works_correct(self):
        self.assertEqual(translate_it('Hello world'), 'Привет мир')

    def test_URL(self):
        params = {
            'key': API_KEY,
            'text': "Hello world",
            'lang': '{}'.format('ru'),
        }
        response = requests.get(URL, params=params)
        self.assertEqual(response.status_code, 200)

    def test_wrong_request(self):
        params = {
            'key': API_KEY,
        }
        response = requests.get(URL, params=params)
        self.assertEqual(response.status_code, 400)

    def test_keyerror(self):
        with self.assertRaises(KeyError):
            translate_it('Hello', '2')


if __name__ == '__main__':
    unittest.main()
