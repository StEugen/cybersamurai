# urls
from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path("", views.index, name='index'),
    path("cabinet_adding/", views.cabinet_adding, name='cabinet_adding'),
    path("cabinet_adding/add", views.add, name='add')
]