from django.shortcuts import render
from .models import News2015
# Create your views here.

def news_view(request):
    news2015 = News2015.objects.all()
    return render(request, "news_index.html", {"news2015": news2015})
