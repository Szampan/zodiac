from django.shortcuts import render
from django.http import HttpResponse

from .models import Sign
from .forms import BirthdayForm
from .tools import *

def index(request):

    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        context = {'form': form} 
        if form.is_valid():
            sign = get_sign(form.cleaned_data['birthday'])
            context['db_sign'] = Sign.objects.get(name=sign)    
        return render(request, 'zodiacs/index.html', context)
    else:
        form = BirthdayForm()
    return render(request, 'zodiacs/index.html', {'form': form})
           


    