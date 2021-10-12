from django.db import models

# Create your models here.
class Posts(models.Model):
	title=models.CharField(max_length=120)
	shortdesc=models.CharField(max_length=600)
	longdesc=models.TextField()
	image=models.ImageField(upload_to='postimages', blank=True)
	def __str__(self):
		return f"{self.title}"
# Create your models here.
