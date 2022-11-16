from django.contrib import admin
from django.urls import path
from accident import views

urlpatterns = [
    path("year", views.accident_view),
    path("local", views.accident_local),
]