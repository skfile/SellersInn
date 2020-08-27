from django.shortcuts import render
from django.http import HttpResponse
# from django.db.models import Q
from .forms import DataForm
from .models import *
from .forms import *


def home(request):
    context = {}
    return render(request, 'main/Home.html', context)


def about(request):
    context = {}
    return render(request, 'main/about.html', context)


def sample1(request):
    context = {}
    return render(request, 'main/sample1.html', context)


def sample2(request):
    context = {}
    return render(request, 'main/sample2.html', context)


def sample3(request):
    context = {}
    return render(request, 'main/sample3.html', context)


def register(request):
    context = {}
    return render(request, 'main/signup.html', context)

# def store(request):
    # products = crawledData.objects.all()

    # return render(request, 'main/Store.html', {'products': products})
