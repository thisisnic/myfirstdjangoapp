from django.conf import settings
from django.db import models
from django.utils import timezone

# This line defines our model - it is an  object
# Post is the name of our model
# models.Model means that the Post is a Django model so Django knows it should be save in the database
class Post(models.Model):

	# Next we define its properties
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	# def means that this is a function/method 
	# this method has a side-effect (self.save)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	# This method returns something - self.title
	def __str__(self):
		return self.title
		