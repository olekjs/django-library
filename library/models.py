from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Book(models.Model):
	isbn         = models.IntegerField()
	title        = models.CharField(max_length=200)
	author       = models.CharField(max_length=200)
	photo_link   = models.CharField(max_length=1000)
	description  = models.TextField()
	category     = models.ForeignKey(Category, on_delete=models.CASCADE)
	number_pages = models.IntegerField()
	edition_date = models.DateTimeField()
	is_reserved  = models.CharField(max_length=2, default='no')

	def __str__(self):
		return self.title

	def slug(self):
		return self.title.replace(' ', '-').lower()

class Reservation(models.Model):
	user       = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	book       = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
	from_date  = models.DateField()
	to_date    = models.DateField()
	created_at = models.DateTimeField(default=timezone.now)
