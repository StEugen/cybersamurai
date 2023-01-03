from django.shortcuts import render
from django.http import HttpResponse
from list.models import *

def index(request):
    data = cabinets.objects.all()
    print(data)
    item = {
        'cabinet': data,
    }
    print(item)
    return render(request, 'index.html', item)
