import unittest
from flask import Flask, request


class TestBasic(unittest.TestCase):
    def test_get_articles(self):
        r = request.get('https://flaskreact-native-test.herokuapp.com/get')

        if r.status_code != 200:
            return r.status_code, ''
        else:
            response_data = r.json()
            return r.status_code, response_data["'https://flaskreact-native-test.herokuapp.com/get"]


if __name__ == '__main__':
    unittest.main()