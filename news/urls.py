from django.urls import path
from news import views

urlpatterns = [
    path("1", views.news_view),
]
