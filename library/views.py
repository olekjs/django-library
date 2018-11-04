from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
	Book, 
	Reservation,
	Category)
from .forms import RentBook
from django.views.generic import ListView
import datetime


class BookListView(ListView):
	model = Book
	template_name = 'main/index.html'
	context_object_name = 'books'


def showBook(request, book_id):
	book = getBook(book_id)

	if request.method == 'POST':
		form = RentBook(request.POST)
		form.setBookInForm(book_id)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.book = book
			post.save()
			messages.success(request, f'Book has been reserved!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		else:
			messages.error(request, f'Reservation was unsuccessful. Wrong data')

	form = RentBook()
	reservations = Reservation.objects.filter(book_id=book)

	return render(request, 'book/show.html', {'book': book, 'form': form, 'reservations': reservations})


def getBook(id):
	return Book.objects.get(id=id)

def reservationsList(request):

	if request.method == 'POST':
		reservation_id = request.POST.get("deleteReservation")
		Reservation.objects.filter(id=reservation_id).delete()
		messages.success(request, f'Reservation has been deleted!')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	else:
		reservations = Reservation.objects.filter(user=request.user)
		return render(request, 'reservations/index.html', {'reservations': reservations})

def categories(request):
	categories = Category.objects.all()
	books = None
	if request.method == 'POST':
		books = Book.objects.filter(category_id=request.POST.get("category"))

	return render(request, 'categories/index.html', {'categories': categories, 'books': books})