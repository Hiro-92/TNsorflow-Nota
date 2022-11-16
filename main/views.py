from django.shortcuts import render
from .models import Main

def main_map(request):
    return render(request, "map.html")
