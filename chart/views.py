from django.shortcuts import render
from .models import Covid
from django.db.models import Count, Q


def home(request):
    return render(request, 'home.html')


def covid(request):
    return render(request, 'covid.html')


def covid2(request):
    return render(request, 'covid2.html')


def covid3(request):
    return render(request, 'covid3.html')
