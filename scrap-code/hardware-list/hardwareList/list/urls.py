# urls
from django.urls import path
from . import views
from list.views import MainView, PostView

app_name = 'list'
urlpatterns = [
    path("", MainView.as_view(), name='index'),
    path('hard-json/', PostView.as_view(), name="hard-json")
]