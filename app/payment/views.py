from django.shortcuts import render
from payment.serializers import PaymentSerializer
from core.models import Loan
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
import http
from payment.helpers import get_annual_interest

@api_view(['POST'])
def add_payment(request):
    data = {}
    try:
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.data['amount']
            date = serializer.data['date']
            try:
                loan = 	Loan.objects.get(cleared=0)	

            except:
                data['message'] = "No loan has been initiated yet."
                return JsonResponse(data, status=http.HTTPStatus.OK)
            
            interest = 	get_annual_interest(loan.amount, loan.interest, loan.date, date)
            amount_with_annual_interest = loan.amount + interest	
            new_amount = amount_with_annual_interest - amount
            loan.amount = new_amount
            loan.date = date
            loan.save()
            data['message'] = f"An amount of {amount} has been added successfully"
            data['balance'] = new_amount
            return JsonResponse(data, status=http.HTTPStatus.OK)
        else:
            data['message'] = serializer.errors
            return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)
    except Exception as e:
        data['message'] = str(e)
        return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)
		
