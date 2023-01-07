from django.http import JsonResponse
from list.models import *
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class MainView(LoginRequiredMixin, TemplateView):
    login_url = 'admin/'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        cabs = cabinets.objects.all()
        context = {
            'cabinets': cabs
        }
        return context
    


class PostView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        hardware = list(Hardware.objects.values())
        cabs = list(cabinets.objects.values())
        return JsonResponse(
            {
                'cabs': cabs,
                'hard': hardware
            }, safe=False
        )

