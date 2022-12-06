from django.urls import path
from . import views

app_name = 'testapp'
urlpatterns = [
    path('', views.index, name=index)
]