from django.http import HttpResponse
from .models import Advertisement
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def lessonFour(request):
    return HttpResponse("Урок номер 4")

def top_sellers(request):
    return render(request, 'top-sellers.html')

def index(request):
    advertisements = Advertisement.objects.all()