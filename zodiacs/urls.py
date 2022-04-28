from django.urls import path

from . import views

app_name = 'zodiacs'
urlpatterns = [
    path('', views.index, name='index'),
    # path('results/', views.results, name='results'),
    # path ('test_form/', views.test_form, name='test_form'),
]