from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.models import Loan
from loan.serializers import LoanSerializer
from rest_framework import status
import http


@api_view(['POST'])
def initiate_loan(request):
	""" initiate loan api view 
		:param request: an object containing the user's request
	"""
	
	data = {}
	try:
		serializer = LoanSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			data['message'] = "A loan has been initiated"
			return JsonResponse(data, status=http.HTTPStatus.OK) 
		else:
			data['message'] = serializer.errors
			return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)

	except Exception as e:
		data['message'] = str(e)
		return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)

