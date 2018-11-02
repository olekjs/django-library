from django import forms
from .models import Reservation
import datetime

class RentBook(forms.ModelForm, book_id):
	def clean(self):
		cleaned_data = super(RentBook, self).clean()

		from_date = cleaned_data.get('from_date')
		to_date = cleaned_data.get('to_date')
		#todo get book!
		print(Reservation.objects.filter(to_date__range=(from_date, to_date), from_date__range=(from_date, to_date) ).count() )

		if from_date < datetime.date.today() or to_date < from_date:
			self.add_error('from_date', f'Wrong data')
		elif Reservation.objects.filter(to_date__range=(from_date, to_date), from_date__range=(from_date, to_date), book=book ).count() > 0:
			self.add_error('from_date', f'Wrong data')

		return cleaned_data

	class Meta:
		model = Reservation
		fields = ['from_date', 'to_date']
		widgets = {
			'from_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
			'to_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
		}