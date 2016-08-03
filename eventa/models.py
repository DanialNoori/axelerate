from django.db import models

# Create your models here.
class Event(models.Model):

	name = models.CharField(max_length=150)
	description = models.TextField()
	url = models.CharField(max_length=200, default='/')
	eventImage = models.ImageField(upload_to='media/', blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	fadate = models.CharField(max_length=150, blank=True, null=True)

	def __str__(self):
		return self.name
