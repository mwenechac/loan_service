import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Loan


class GetBalanceTestCase(APITestCase):
	'''
		A get balance unit test used to test the 
		get balance api on an existing loan.
	'''
	def setUp(self):
		loans = Loan.objects.filter().update(cleared=1)
		loan = Loan(
			amount = 1000,
			interest = 10,
			date = "2021-01-26"
		)
		loan.save()
		self.test_get_balance()

	def test_get_balance(self):
		data = {
			"date": "2023-01-26"
		}
		response = self.client.get("/balance/get-balance", data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)