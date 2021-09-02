import unittest
import requests
import json
import hello

# At the moment all tests are manipulating existing data in the DB - this needs to be restructured to only test the functionality without manipulating data.


class TestAPI(unittest.TestCase):
    URL = 'https://flaskreact-native-test.herokuapp.com/'

    def test_1_get_all(self):
        resp = requests.get(self.URL + '/get')
        self.assertEqual(resp.status_code, 200)
        # if delete test does not delete, this must be incremented
        # self.assertEqual(resp.json())
        print(resp.json())
        print("Test 1 completed, all articles expected recieved")
        # print(resp.json())
    def test_2_get_specific_article(self):
        # must be respecified if specific article is deleted
        resp = requests.get(self.URL + '/get/' +'/66')
        self.assertEqual(resp.status_code, 200)
        # print(resp.json())
        print("Test 2 Completed, retrieved specific article")
    def test_3_delete(self):
        # for now, this id must be re-specified every time it's called - best bet if Post is working to +1 to last id
        resp = requests.delete(self.URL + '/delete/' '/106'  )
        self.assertEqual(resp.status_code, 200)
        # print(resp.json())
        print("Test 3 Completed, delete succesful")

    #  successfuly posts a new article
    def test_4_post(self):
        # creates a test post, new incremented ID assigned
        resp = requests.post(self.URL + '/add',
        json={'title':'Testing POST Title', 'body':'Testing POST Body'})
        self.assertEqual(resp.status_code, 200)
        print("test 4 completed successfully")
        print (resp.json())
        # if printed resp.json doesn't return a date or id something is broken
        # from Jordan:
        # after post is made, is the row present in the database ^ confirmed in the printed response above

        # test test trying to create a test enviroment
    # def test_1a_get_all(self):
    #     tester = hello.test_client(self)
    #     resp = requests.get(self.URL + '/get')
    #     self.assertEqual(resp.status_code, 200)
    #     # if delete test does not delete, this must be incremented
    #     # self.assertEqual(len(resp.json()))
    #     print(resp.json())
    #     print("Test 1a completed, all articles expected recieved within a test environment")
    #     # print(resp.json())











if __name__ == '__main__':
    unittest.main()