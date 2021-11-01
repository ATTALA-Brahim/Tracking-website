from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
	
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	
    
	def __str__(self):
		return self.name



class Location(models.Model):
	

	longitude = models.CharField(max_length=200, null=True)
	latitude = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	device = models.ForeignKey(Device, null=True, on_delete= models.SET_NULL)
    