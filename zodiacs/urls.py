from django.urls import path

from . import views

app_name = 'zodiacs'
urlpatterns = [
    path('', views.IndexFormView.as_view(), name='index'),
    # path('', views.index, name='index'),
]