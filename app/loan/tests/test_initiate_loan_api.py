from rest_framework.test import APITestCase

from rest_framework import status


class InitiateLoanTestCase(APITestCase):
    '''
		A unit test to test the initiate loan api.
        Date, interest and amount are used to create a json object 
        which is use in the post method method to simulate the api
	'''
    def setUp(self):
        self.test_initiate_loan()

    def test_initiate_loan(self):
        data = {
            "amount": 1000,
            "interest": 10,
            "date": "2022-01-28"
        }
        response = self.client.post("/loan/initiate", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
