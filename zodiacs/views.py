from django.shortcuts import render

from .models import Sign

from .tools import *


def index(request):
    if request.method == 'POST':
        input = request.POST.get('birthday')
        context = {}  
        db_error_message = 'Ups, coś poszło nie tak... '

        if '30/02' in input:                                 
            try:
                context['db_sign'] = Sign.objects.get(name='Dinozaur')
            except:
                context['db_sign'] = db_error_message 
            return render(request, 'zodiacs/index.html', context)                          
    
        if is_input_valid(input):
            sign = get_sign(input)
            try:
                context['db_sign'] = Sign.objects.get(name=sign)    
            except:
                context['db_sign'] = db_error_message + sign
        else:
            context['invalid_input'] = 'Nieprawidłowy format daty'   

        return render(request, 'zodiacs/index.html', context)
    return render(request, 'zodiacs/index.html')


# def is_input_valid(input):
#     format = '%d/%m/%Y'
#     valid = True
#     try:
#         valid = bool(datetime.strptime(input, format))
#     except ValueError:
#         valid = False
#     return valid


    