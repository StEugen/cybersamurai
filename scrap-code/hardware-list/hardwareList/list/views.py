from django.shortcuts import render
from django.http import HttpResponse
from list.models import *

def index(request):
    data = cabinets.objects.all()
    context = {
        'cabinets': data
    }
    return render(request, 'index.html', context)
