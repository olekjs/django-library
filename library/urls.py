from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	path('', views.BookListView.as_view(), name='home-page'),
	path('book/<int:book_id>', views.showBook, name='show-book'),
	path('reservations', login_required(views.reservationsList), name='reservations-list'),
	path('categories', views.categories, name='categories'),
]

