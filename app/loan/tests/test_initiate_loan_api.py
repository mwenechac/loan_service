from rest_framework.test import APITestCase

from rest_framework import status


class InitiateLoanTestCase(APITestCase):
    def setUp(self):
        self.test_initiate_loan()

    def test_initiate_loan(self):
        data = {
            "amount": 1000,
            "interest": 10,
            "date": "2022-01-26"
        }
        response = self.client.post("/loan/initiate-loan", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
