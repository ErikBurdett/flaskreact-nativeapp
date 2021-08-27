import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = 'https://flaskreact-native-test.herokuapp.com/get'
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
    def test_1_get_all(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 4)
        print("Test 1 completed")
        print(resp)
        if resp == self.data:
            return print('data is correct')
        else:
            return print('Something is different')
    # def test_2_post_details(self):
    #     resp = requests.post(self.URL, json = self.data)
    #     self.assertEqual(resp.status_code, 200)
    #     # self.assertDictEqual(res.dict(), self.data)
    #     print("Test 2 Completed")



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
    tester = TestAPI()
    tester.test_1_get_all()
    unittest.main()