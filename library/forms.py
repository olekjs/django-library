from django import forms
from .models import Reservation, Book
from datetime import date
import datetime


class RentBook(forms.ModelForm):

	def setBookInForm(self, book_id):
		self.book_id = book_id

	def clean(self):
		cleaned_data = super(RentBook, self).clean()

		from_date = cleaned_data.get('from_date')
		to_date = cleaned_data.get('to_date')
		book = Book.objects.get(id=self.book_id)
		one_month_limit = to_date - from_date

		if from_date < datetime.date.today() or to_date < from_date or one_month_limit.days > 30:
			self.add_error('from_date', f'Wrong data')
		elif Reservation.objects.filter(to_date__gte=from_date, from_date__lte=to_date, book=book).count() > 0:
			self.add_error('from_date', f'Wrong data')

		return cleaned_data

	class Meta:
		model = Reservation
		fields = ['from_date', 'to_date']
		widgets = {
			'from_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
			'to_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
		}