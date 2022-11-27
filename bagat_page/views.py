from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return render(request, "bagat_page/index.html")

def info(request):
    return render(request, "bagat_page/info.html")

def advantages(request):
    return render(request, "bagat_page/advantages.html")

def priority_directions(request):
    return render(request, "bagat_page/priority_directions.html")