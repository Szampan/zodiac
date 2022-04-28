from datetime import datetime     

from django.shortcuts import render

from .models import Sign


def index(request):
    if request.method == 'POST':
        input = request.POST.get('birthday')
        context = {}  
        db_error_message = 'Ups, coś poszło nie tak...'

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
                context['db_sign'] = db_error_message 
        else:
            context['invalid_input'] = 'Nieprawidłowy format daty'   

        return render(request, 'zodiacs/index.html', context)
    return render(request, 'zodiacs/index.html')


def is_input_valid(input):
    format = '%d/%m/%Y'
    valid = True
    try:
        valid = bool(datetime.strptime(input, format))
    except ValueError:
        valid = False
    return valid


def get_sign(input):
    date = datetime.strptime(input, '%d/%m/%Y')
    month, day = date.month, date.day
    if month == 1:
        if day <= 19:
            return 'Koziorożec'
        else:
            return 'Wodnik'
    elif month == 2:
        if day <= 18:
            return 'Wodnik'
        else:
            return 'Ryby'
    elif month == 3:
        if day <= 20:
            return 'Ryby'
        else:
            return 'Baran'
    elif month == 4:
        if day <= 19:
            return 'Baran'
        else:
            return 'Byk'
    elif month == 5:
        if day <= 20:
            return 'Byk'
        else:
            return 'Bliźnięta'
    elif month == 6:
        if day <= 20:
            return 'Bliźnięta'
        else:
            return 'Rak'
    elif month == 7:
        if day <= 22:
            return 'Rak'
        else:
            return 'Lew'
    elif month == 8:
        if day <= 22:
            return 'Lew'
        else:
            return 'Panna'
    elif month == 9:
        if day <= 22:
            return 'Panna'
        else:
            return 'Waga'
    elif month == 10:
        if day <= 22:
            return 'Waga'
        else:
            return 'Skorpion'
    elif month == 11:
        if day <= 21:
            return 'Skorpion'
        else:
            return 'Strzelec'
    elif month == 12:
        if day <= 21:
            return 'Strzelec'
        else:
            return 'Koziorożec'
    else:
        return 'Invalid month'
    


