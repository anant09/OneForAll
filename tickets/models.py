from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tickets(models.Model):
	journey_id=models.BigIntegerField(default=1)
	PNR= models.BigIntegerField()
	train_no=models.BigIntegerField()
	date=models.DateTimeField()
	price=models.BigIntegerField()
	train_name=models.CharField(max_length=200)
	location_from=models.CharField(max_length=200)
	location_to=models.CharField(max_length=200)
	
	def __str__(self):
		return self.train_name

	
# Create your models here.
