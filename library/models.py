from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Book(models.Model):
	isbn         = models.IntegerField()
	title        = models.CharField(max_length=200)
	author       = models.CharField(max_length=200)
	photo_link   = models.CharField(max_length=300)
	description  = models.TextField()
	category     = models.ForeignKey(Category, on_delete=models.CASCADE)
	number_pages = models.IntegerField()
	edition_date = models.DateTimeField()

	def __str__(self):
		return self.title

	def slug(self):
		return self.title.replace(' ', '-').lower()

	def isRent(self):
		today = datetime.date.today()
		if Reservation.objects.filter(book=self.id, to_date__gte=today, from_date__lte=today).count() != 0:
			return True

class Reservation(models.Model):
	user       = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	book       = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
	from_date  = models.DateField()
	to_date    = models.DateField()
	created_at = models.DateTimeField(default=timezone.now)

	def is_future(self):
		return self.from_date > datetime.date.today()

	def is_future_and_active(self):
		return self.from_date > datetime.date.today() - datetime.timedelta(days=30)