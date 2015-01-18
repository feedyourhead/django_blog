from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=180)
	content =models.TextField()
	likes = models.IntegerField(default=0)
	draft =models.BooleanField(default=True)
	pub_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.title

class Comments(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=200)
	content = models.TextField()
	publication_date =models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content+" by "+ self.author