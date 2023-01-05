from django.shortcuts import render
from django.http import HttpResponse
from list.models import *

def index(request):
    data = cabinets.objects.all()
    return render(request, 'index.html', { 'cabinets': data })



def display(request):
    if request.method == "POST":
        data = cabinets.objects.all()
        return HttpResponse(data)