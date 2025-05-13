from django.shortcuts import render

# Create your views here.
# food/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'hdgroup/index.html', context=None)