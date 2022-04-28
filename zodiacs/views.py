from datetime import datetime       # test

from django.shortcuts import render
# from django.http import HttpResponse    # test

from .models import Sign

# from .forms import BirthForm

# def index(request):
#     return render(request, 'zodiacs/index.html')

# def index(request):
#     if request.method == "POST":
#         birthday = request.POST.get('birthday')
#         if birthday:
#             context = {'birthday': birthday}
#             return render(request, 'zodiacs/index.html', context)

#     return render(request, 'zodiacs/index.html')



def index(request):
    if request.method == "POST":
        input = request.POST.get('birthday')
        context = {'input': input}  # test          # docelowo: {}
        db_error_message = "Ups, coś poszło nie tak"

        if '30/02' in input:
            context['date'] = (30, 2)               # temp
            context['sign'] = 'Dinozaur'            # temp
            try:
                context['db_sign'] = Sign.objects.get(name='Dinozaur')
            except:
                context['db_sign'] = db_error_message
            return render(request, 'zodiacs/index.html', context)
             
        format = "%d/%m/%Y"
        valid = True
        try:
            valid = bool(datetime.strptime(input, format))
        except ValueError:
            valid = False
        context['valid'] = valid

        if valid:
            date = datetime.strptime(input, "%d/%m/%Y")
            sign = get_sign(date.month, date.day)

            context['date'] = date.month, date.day      # temp
            context['sign'] = sign                      # temp
            signs = Sign.objects.order_by('id')         # temp  
            context['db_signs'] = signs                 # temp

            try:
                context['db_sign'] = Sign.objects.get(name=sign)    
            except:
                context['db_sign'] = db_error_message

            ####
                   
        return render(request, 'zodiacs/index.html', context)
    return render(request, 'zodiacs/index.html')


def test_form(request):
    if request.method == "POST":
        input = request.POST.get('username')
        if input == "mark":
            # return HttpResponse('hello mark')
            context = {'username': input}
            return render(request, 'zodiacs/test_form.html', context)
             
        format = "%d/%m/%Y"
        valid = True
        try:
            valid = bool(datetime.strptime(input, format))
        except ValueError:
            valid = False
                    
        context = {'test_str': input, 'valid': valid}
        if valid:
            date = datetime.strptime(input, "%d/%m/%Y")
            context['date'] = int(date.strftime("%m")), int(date.strftime("%d"))       
            context['sign'] = get_sign(int(date.strftime("%m")), int(date.strftime("%d")))
                   
        return render(request, 'zodiacs/test_form.html', context)
    return render(request, 'zodiacs/test_form.html')



def get_sign(month, day):
    if month == 1:
        if day <= 20:
            return "Koziorożec"
        else:
            return "Wodnik"
    elif month == 2:
        if day <= 19:
            return "Wodnik"
        else:
            return "Ryby"
    elif month == 3:
        if day <= 20:
            return "Ryby"
        else:
            return "Baran"
    elif month == 4:
        if day <= 20:
            return "Baran"
        else:
            return "Byk"
    elif month == 5:
        if day <= 21:
            return "Byk"
        else:
            return "Bliźnięta"
    elif month == 6:
        if day <= 21:
            return "Bliźnięta"
        else:
            return "Rak"
    elif month == 7:
        if day <= 22:
            return "Rak"
        else:
            return "Lew"
    elif month == 8:
        if day <= 23:
            return "Lew"
        else:
            return "Panna"
    elif month == 9:
        if day <= 23:
            return "Panna"
        else:
            return "Waga"
    elif month == 10:
        if day <= 23:
            return "Waga"
        else:
            return "Skorpion"
    elif month == 11:
        if day <= 22:
            return "Skorpion"
        else:
            return "Strzelec"
    elif month == 12:
        if day <= 21:
            return "Strzelec"
        else:
            return "Koziorożec"
    else:
        return "Invalid month"
    

# def results(request):
#     # inp_value = request
#     inp_value = request.GET.get('results', 'Default value')
#     context = {'inp_value': inp_value, "form": 'Birthform function'}
#     return render(request, 'zodiacs/results.html', context)

# def test_form(request):
#     context ={}
#     form = BirthForm()
#     context['form']= form
#     if request.GET:
#         temp = request.GET['birth_field']
#         print(type(temp))
#     return render(request, "zodiacs/test_form.html", context)
