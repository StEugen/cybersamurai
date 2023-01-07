from django.shortcuts import render
from django.http import JsonResponse
from list.models import *
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import user_passes_test


class MainView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        cabs = cabinets.objects.all()
        context = {
            'cabinets': cabs
        }
        return context
    


class PostView(View):
    def get(self, *args, **kwargs):
        hardware = list(Hardware.objects.values())
        cabs = list(cabinets.objects.values())
        return JsonResponse(
            {
                'cabs': cabs,
                'hard': hardware
            }, safe=False
        )

