from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from .models import Book
from .forms import RentBook

def home(request):
	context = {
		'books': Book.objects.all()
	}

	return render(request, 'main/index.html', context)


def showBook(request, book_id, slug):
	if request.method == 'POST':
		form = RentBook(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('asd')

	context = {
		'book': getBook(book_id),
		'formRent': RentBook()
	}

	return render(request, 'book/show.html', context)

def getBook(id):
	return Book.objects.filter(id=id).get()