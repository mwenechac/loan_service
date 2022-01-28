from rest_framework import serializers
from core.models import Loan

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Loan
		fields = ['amount', 'date']
		extra_kwargs = {
            'amount': {'required': True},
            'date': {'required': True}
        }
