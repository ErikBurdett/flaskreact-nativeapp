import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = 'https://flaskreact-native-test.herokuapp.com/'
    data =[{
    "body": "3030!!!",
    "date": "2021-08-27T15:41:44.032828",
    "id": 2,
    "title": "Deltron"
    },
    {
    "body": "Test 4",
    "date": "2021-08-27T17:35:58.872372",
    "id": 4,
    "title": "Test before deployment"
    },
    {
    "body": "Howdy! Edit test\n",
    "date": "2021-08-27T15:41:13.449348",
    "id": 1,
    "title": "DB deployed - 1st test - edit test"
    },
    {
    "body": "Howdy! ",
    "date": "2021-08-27T17:38:54.572090",
    "id": 5,
    "title": "Hello from the deployed application"
    }]

    expected_result_test3 ={
    "body": "3030!!!",
    "date": "2021-08-27T15:41:44.032828",
    "id": 2,
    "title": "Deltron"
}
    def test_1_get_all(self):
        resp = requests.get(self.URL + '/get')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 8)
        print("Test 1 completed")
        print(resp.json())
        if resp == self.data:
            return print('data is correct')
        else:
            return print('Something is different')
    def test_2_get_all(self):
        resp = requests.get(self.URL + '/get', json = self.data)
        self.assertEqual(resp.status_code, 200)
        print(self.data)
        print(resp.json())
        # self.assertDictEqual(resp.dict(), self.data)
        print("Test 2 Completed")
    def test_3_get_specific_article(self):
        resp = requests.get(self.URL + '/get/' +'/10')
        self.assertEqual(resp.status_code, 200)
        # self.assertDictEqual(resp.json(), self.expected_result_test3)
        print(resp.json())
        print("Test 3 Completed")
    def test_4_delete(self):
        resp = requests.delete(self.URL + '/delete/' '/14')
        self.assertEqual(resp.status_code, 200)
        print(resp.json())
        print("Test 4 Completed")
    # def test_5_post(self):
    #     resp = requests.post(self.URL + '/post/'+'{new_post_obj}')
    #     new_post_obj = {
    #         "body": "DB Test POST request",
    #         "date": "",
    #         "id": 10,
    #         "title": "DB POST TEST"
    #     }
# returning an error 405 !=200
    # def test_5_update(self):




    # # def test_get_articles(self):
    # #     response = request.get(f'https://flaskreact-native-test.herokuapp.com/get')
    # #     if response.ok:
    # #         return response.text
    # #     else:
    # #         return 'Bad Response!'
    # def test_get_articles(self):
    #     with patch('articles.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'




if __name__ == '__main__':
    unittest.main()