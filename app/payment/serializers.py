from rest_framework import serializers
from core.models import Loan

class PaymentSerializer(serializers.ModelSerializer):
	'''
		A payment serialier class used to convert
		the request object into a native Python datatype
		that can then be easily rendered into JSON
	'''
	class Meta:
		model = Loan
		fields = ['amount', 'date']
		extra_kwargs = {
            'amount': {'required': True},
            'date': {'required': True}
        }
