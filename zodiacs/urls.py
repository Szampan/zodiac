from django.urls import path

from . import views

app_name = 'zodiacs'
urlpatterns = [
    path('', views.index, name='index'),
]