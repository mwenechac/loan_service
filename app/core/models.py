from django.db import models

class Loan(models.Model):
    """ model definition for the loan object """
    
    id = models.BigAutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    interest = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    cleared = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'loan'
