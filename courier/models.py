from django.db import models
from django.contrib.auth.models import User

var = 1
# Create your models here.
class Courier(models.Model):
	id = models.BigIntegerField(default = 0, unique = True, primary_key = True)
	weight= models.BigIntegerField()
	height=models.BigIntegerField()
	width=models.BigIntegerField()
	length=models.BigIntegerField()
	user = models.ForeignKey(User, default=None)
	location_from=models.CharField(max_length=200)
	location_to=models.CharField(max_length=200)
	
	def __str__(self):
		return self.user.username
	