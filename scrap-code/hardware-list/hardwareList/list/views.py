from django.shortcuts import render
from django.http import HttpResponse
from list.models import *
from django.shortcuts import redirect
from django.middleware.csrf import get_token


def index(request):
    data = cabinets.objects.all()
    return render(request, 'index.html', { 'cabinets': data })

def cabinet_adding(request):
    return render(request, 'add.html')

def add(request):
    if request.method =='POST':
        cab = request.POST.get('cab_num')
        nums = request.POST.get('nums')
        nums = nums.split(', ')
        submit_to_db = cabinets(cabinet=cab, hard=nums)
        submit_to_db.save()
        return redirect("list:index")
    
