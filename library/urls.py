from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('book/<int:book_id>/<slug>', views.showBook, name='show-book'),
]
