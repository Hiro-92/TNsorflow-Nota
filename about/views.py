from django.shortcuts import render
from .models import About

def about_view(request):
    abouts = About.objects.all()
    return render(request, "about.html", {"about": abouts})