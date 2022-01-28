from rest_framework import serializers
from core.models import Loan
from datetime import datetime


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
		
	def validate(self, data):
		if data['date'] < datetime.now().date():
			raise serializers.ValidationError({"date": "Date must be greater than or equal to the current date."})
		return data
