import unittest
from hello import homepage

class TestHomepage(unittest.TestCase):
    def test_homepage(self):
        result = type(homepage()) == str
        print("homepage() returns a string: " + str(result) + ": " + str(homepage()))