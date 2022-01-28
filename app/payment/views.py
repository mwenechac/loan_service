from django.shortcuts import render
from payment.serializers import PaymentSerializer
from core.models import Loan
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
import http
from core.helpers import get_annual_interest

@api_view(['POST'])
def add_payment(request):
    '''
		A post method that is used to make a payment.
		param: amount int
		param: date(yyyy-m-dd) str, should be greater or equal to current date
	'''
    
    data = {}

    try:
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_amount = serializer.data['amount']
            date = serializer.data['date']
            try:
                loan = 	Loan.objects.get(cleared=0)
                
            except:
                data['message'] = "No loan has been initiated yet."
                return JsonResponse(data, status=http.HTTPStatus.OK)
            
            if loan.amount <= 0:
                data['message'] = "Payment not accepted. Loan has already been cleared."
                return JsonResponse(data, status=http.HTTPStatus.NOT_ACCEPTABLE)

            interest = 	get_annual_interest(loan.amount, loan.interest, loan.date, date)
            amount_with_annual_interest = loan.amount + interest	
            balance = amount_with_annual_interest - payment_amount
            loan.amount = balance
            loan.date = date
            loan.save()
            data['message'] = f"An amount of {payment_amount} has been added successfully"
            data['balance'] = balance
            return JsonResponse(data, status=http.HTTPStatus.OK)
        else:
            data['message'] = serializer.errors
            return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)
    except Exception as e:
        data['message'] = str(e)
        return JsonResponse(data, status=http.HTTPStatus.BAD_REQUEST)
		
