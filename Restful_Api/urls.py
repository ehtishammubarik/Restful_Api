"""Restful_Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# class contains implementation of api functions
from Restful_Api.api import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', views.ApiOverview.as_view(), name='api'),
        path('authentication/', obtain_auth_token, name='authentication'),
        path('book-list/', views.bookList, name="book-list"),
        path('get-book/<str:pk>/', views.getBook, name="get-book"),
        path('add-book/', views.addBook, name="add-book"),
        path('update-book/<str:pk>/', views.updateBook, name="book-update"),
        path('delete-book/<str:pk>/', views.deleteBook, name="book-delete"),
        path('pdf/', views.PdfFiles.as_view(), name='pdf-files')
] + staticfiles_urlpatterns()
