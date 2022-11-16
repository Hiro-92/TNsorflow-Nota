from django.shortcuts import render
from .models import AccidentGraph, AccidentLocal

# Create your views here.
def accident_view(request):
    accidentview = AccidentGraph.objects.all()
    return render(request,"piechart_year.html", {"accidentview": accidentview})

def accident_local(request):
    accidentlocal = AccidentLocal.objects.all()
    return render(request, "barchart_local.html", {"accidentlocal": accidentlocal})
