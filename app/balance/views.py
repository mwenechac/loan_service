from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from core.helpers import get_annual_interest
from core.models import Loan
import http

@api_view(['GET'])
def get_balance(request):
	data = {}
	try:
		given_date = request.GET.get('date')
		try:
			loan = Loan.objects.get(cleared=0)	
		except:
			data['message'] = "No loan has been initiated yet."
			return JsonResponse(data, status=http.HTTPStatus.OK)
		interest = get_annual_interest(loan.amount, loan.interest, loan.date, given_date)
		amount_with_annual_interest = loan.amount + interest
		data['data'] = {"current_balance": amount_with_annual_interest}
		return JsonResponse(data, status=http.HTTPStatus.OK)

	except Exception as e:
		data['message'] = str(e)
		return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)
