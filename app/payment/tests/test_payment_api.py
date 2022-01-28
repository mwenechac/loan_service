
from core.models import Loan
from rest_framework.test import APITestCase

from rest_framework import status

class AddPaymentTestCase(APITestCase):
	def setUp(self):
		loans = Loan.objects.filter().update(cleared=1)
		loan = Loan(
			amount = 1000,
			interest = 10,
			date = "2022-01-26"
		)
		loan.save()
		self.test_get_balance()

	def test_get_balance(self):
		data = {
			"amount": 500,
			"date": "2022-01-29"
		}
		response = self.client.post("/payment/pay", data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
