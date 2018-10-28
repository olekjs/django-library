from django import forms
from .models import Reservation

class RentBook(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ['from_date', 'to_date']
		widgets = {
			'from_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd-mm-yyyy'}),
			'to_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd-mm-yyyy'}),
		}