from rest_framework import serializers
from core.models import Loan

class LoanSerializer(serializers.ModelSerializer):

	""" 
		A serializer class for changing the loan data
		to native python data type.
	"""

	class Meta:
		model = Loan
		fields = ['amount', 'interest', 'date']
		extra_kwargs = {
            'amount': {'required': True},
            'interest': {'required': True},
            'date': {'required': True}
        }
	
	def save(self):
		loans = Loan.objects.filter().update(cleared=1)
		loan = Loan(
			amount = self.validated_data['amount'],
			interest = self.validated_data['interest'],
			date = self.validated_data['date']
		)

		loan.save()
		return loan