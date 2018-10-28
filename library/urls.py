from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.BookListView.as_view(), name='home-page'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='show-book'),
]

