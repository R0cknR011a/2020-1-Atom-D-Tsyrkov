import unittest
from unittest.mock import patch
import requests
from host.test.html_generator import HTMLGenerator
from host.url_parser.view import get_most_frequent_words
from host.application.http_request import HTTPRequest


class TestHost(unittest.TestCase):
    def test_word_count(self):
        generator = HTMLGenerator('ENG')
        generator.dictionary = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'life', 'hand']
        text = generator.get_text(15, 30, 100)
        other = generator.hashmap
        result = get_most_frequent_words(text, 'all')
        self.assertEqual(result, other)

        generator.reset_hashmap()
        self.assertEqual(generator.hashmap, {})
        text = generator.get_text(15, 30, 100)
        result = get_most_frequent_words(text, 10)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 10)
        for key, value in result.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, int)

    @patch('http.server.BaseHTTPRequestHandler')
    def test_http_request(self, mock_constructor):
        m_obj = mock_constructor.return_value
        m_obj.client_address = '1.2.3.4', '5555'
        m_obj.command = 'GET'
        m_obj.path = '/this/is/amazing/string?a=5&b=7'
        m_obj.app = 'this'
        m_obj.headers = {'Content-Length': 10}
        m_obj.rfile.read.return_value = b'a=10&b=13'
        request = HTTPRequest(m_obj)
        self.assertEqual(request.method,'GET')
        self.assertEqual(request.path, '/this/is/amazing/string?a=5&b=7')
        self.assertEqual(request.GET, {'a': '5', 'b': '7'})
        self.assertEqual(request.POST, {'a': '10', 'b': '13'})

    def test_request(self):
        response = requests.get('http://localhost:7777/somethingwrongurl')
        self.assertEqual(response.status_code, 404)
        result = response.json()
        self.assertIn('error', result)

        response = requests.get('http://localhost:7777/parser/somethingwrongulr')
        self.assertEqual(response.status_code, 400)
        result = response.json()
        self.assertIn('error', result)

        to_post = {'some': 'thing'}
        response = requests.post('http://localhost:7777/parser/somethingwrongurl', data=to_post)
        self.assertEqual(response.status_code, 403)
        result = response.json()
        self.assertIn('error', result)

    def test_y_count_html(self):
        response = requests.get('http://localhost:7777/parser/?url=http://localhost:8888/&k=10')
        self.assertEqual(response.status_code, 200)
        result = response.json()['result']
        self.assertEqual(len(result), 10)
        self.assertIsInstance(result, dict)
        print(result)

if __name__ == '__main__':
    unittest.main()
