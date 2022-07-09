from django.db import models
from authentication.models import account

# Create your models here.

class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    date = models.DateField()
    from_user = models.ForeignKey(account, on_delete=models.CASCADE)
    to_user = models.CharField(default="", max_length=30)
    jocund = models.IntegerField(default=0)
