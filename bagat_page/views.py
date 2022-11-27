from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return render(request, "bagat_page/index.html")

def info(request):
    return HttpResponse("bebebebe")