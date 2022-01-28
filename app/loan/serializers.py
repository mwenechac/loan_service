from datetime import datetime
from rest_framework import serializers
from core.models import Loan

class LoanSerializer(serializers.ModelSerializer):

	'''
		A loan serialier class used to convert
		the request object into a native Python datatype
		that can then be easily rendered into JSON content type.
	'''

	class Meta:
		model = Loan
		fields = ['amount', 'interest', 'date']
		extra_kwargs = {
            'amount': {'required': True},
            'interest': {'required': True},
            'date': {'required': True}
        }
	
	def validate(self,data):
		if data['date'] < datetime.now().date():
			raise serializers.ValidationError(
				{'data': 'Date must be greater than or equal to the current date.'}
			)
		return data
		
	def save(self):
		loans = Loan.objects.filter().update(cleared=1)
		loan = Loan(
			amount = self.validated_data['amount'],
			interest = self.validated_data['interest'],
			date = self.validated_data['date']
		)

		loan.save()
		return loan