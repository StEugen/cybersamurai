from django.shortcuts import render
from django.http import HttpResponse
from list.models import *
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import user_passes_test


class MainView(TemplateView):
    template_name = 'index.html'

class PostView(View):
    def get(self, *args, **kwargs):
        pass


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    cabs = cabinets.objects.all()
    hard = Hardware.objects.all()
    return render(request, 'index.html', { 
        'cabinets': cabs,
        'hardware': hard 
    })



@user_passes_test(lambda u: u.is_superuser)
def cabinet_adding(request):
    return render(request, 'add.html')

@user_passes_test(lambda u: u.is_superuser)
def add(request):
    if request.method =='POST':
        cab = request.POST.get('cab_num')
        name = request.POST.get('name')
        nums = request.POST.get('nums')
        name = name.split(', ')
        nums = nums.split(', ')
        submit_to_db = cabinets(cabinet=cab)
        submit_to_db.save()
        return redirect("list:cabinet_adding")

@user_passes_test(lambda u: u.is_superuser)
def delete_cabinet(request, cabinet_id):
    instance = cabinets.objects.get(id=cabinet_id)
    instance.delete()
    return redirect("list:index")