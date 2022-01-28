from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.models import Loan
from loan.serializers import LoanSerializer
from rest_framework import status
import http


@api_view(['POST'])
def initiate_loan(request):
	'''
		A post method that is used to initiate a loan.
		param: amount int
		param: date(yyyy-m-dd) str, should be greater or equal to current date
		param: interest int
	'''
	
	data = {}
	try:
		serializer = LoanSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			data['message'] = "A loan has been initiated successfully!"
			return JsonResponse(data, status=http.HTTPStatus.OK) 
		else:
			data['message'] = serializer.errors
			return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)

	except Exception as e:
		data['message'] = str(e)
		return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)

