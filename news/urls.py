from django.contrib import admin
from django.urls import path, include
from news import views

urlpatterns = [
    path("1", views.news_view),
]
