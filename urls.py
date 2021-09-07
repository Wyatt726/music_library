from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.Music_Library.as_view())
    path('music/<int:pk>/, views.Music_Library.as_view())
]


