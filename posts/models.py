from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	owner = models.ForeignKey(
    User, related_name="posts", on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length = 120)
	description = models.TextField()
	img_path = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

