from django.db import models
import datetime
from django.utils import timezone

class Episode(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	ep_num = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

	def __str__(self):
		return str(self.name) + " | Episode - " + str(self.ep_num)

class Watch(models.Model):
	link = models.URLField(null=True, blank=True)
	episode = models.ForeignKey(Episode, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.episode.name)+ " | Episode - "+ str(self.episode.ep_num)


class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Anime(models.Model):
	photo = models.ImageField(upload_to='images', default='#')
	title = models.CharField(null=True, blank=True, max_length=100)
	description = models.TextField(null=True, blank=True)
	season = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
	eps_link = models.ManyToManyField(Episode)
	genre = models.ForeignKey(Genre, default=None, on_delete=models.CASCADE)
	author =  models.ForeignKey(Author, default=None, on_delete=models.CASCADE)
	type = models.ForeignKey(Type, default=None, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published') 

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)