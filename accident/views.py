from django.shortcuts import render
from .models import AccidentGraph, AccidentLocal

# Create your views here.
def accident_view(request):
    accidentview = AccidentGraph.objects.all()
    accidentlocal = AccidentLocal.objects.all()
    return render(request,"chart_index.html", {"accidentview": accidentview, "accidentlocal": accidentlocal})

