from unittest import mock
import requests
import unittest

class MyClass:
    # function get - general
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()

# This method will be used by the mock to replace requests.get
# Create the owner request.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        def json(self):
            return self.json_data
    
    if args[0] == 'http://url-1.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://url-2.com/test.json':
        return MockResponse({"key2": "value2"}, 200)
    
    return MockResponse(None, 404)

# Our test case class
class MyClassTestCase(unittest.TestCase):
    # We patch 'requests.get' with our own method. The mock object is
    # passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        my_class = MyClass()
        # call to url-1
        json_data = my_class.fetch_json('http://url-1.com/test.json')
        print("\nValor:",json_data)    
        self.assertEqual(json_data, {"key1": "value1"})
        # call to url-2
        json_data = my_class.fetch_json('http://url-2.com/test.json')
        self.assertEqual(json_data, {"key2": "value2"})
        # call to url-3 that we did not mock
        json_data = my_class.fetch_json('http://url-3.com/test.json')
        self.assertIsNone(json_data)

if __name__ == '__main__':
    unittest.main()
"""
$ python3 unit_test_mocks.py
Valor: {'key1': 'value1'}
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

"""