from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Reservation
from .forms import RentBook
from django.views.generic import (
	ListView, 
	DetailView,
)

class BookListView(ListView):
	model = Book
	template_name = 'main/index.html'
	context_object_name = 'books'


class BookDetailView(DetailView):
	model = Book
	template_name = 'book/show.html'


def rentBook(LoginRequiredMixin):
	redirect('home-page')
