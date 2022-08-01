from django.db import models
from datetime import datetime, date
# Create your models here.

class Todo(models.Model):
	date = models.DateField(auto_now_add=False, auto_now=False,blank=True)
	time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
	title = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.date)+str(self.time)+ self.title
