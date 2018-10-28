from django.contrib import admin
from django.urls import path, include
from .views import register
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('library.urls')),
]
