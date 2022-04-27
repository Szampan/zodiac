from django.shortcuts import render
# from django.http import HttpResponse    # test

from datetime import datetime       # test

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
        context = {'input': input}

        if '30/02' in input:
            context['date'] = (30, 2)
            context['sign'] = 'Dinosaur'
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
            context['date'] = date.month, date.day    
            context['sign'] = get_sign(date.month, date.day)
                   
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
            return "Capricorn"
        else:
            return "Aquarius"
    elif month == 2:
        if day <= 19:
            return "Aquarius"
        else:
            return "Pisces"
    elif month == 3:
        if day <= 20:
            return "Pisces"
        else:
            return "Aries"
    elif month == 4:
        if day <= 20:
            return "Aries"
        else:
            return "Taurus"
    elif month == 5:
        if day <= 21:
            return "Taurus"
        else:
            return "Gemini"
    elif month == 6:
        if day <= 21:
            return "Gemini"
        else:
            return "Cancer"
    elif month == 7:
        if day <= 22:
            return "Cancer"
        else:
            return "Leo"
    elif month == 8:
        if day <= 23:
            return "Leo"
        else:
            return "Virgo"
    elif month == 9:
        if day <= 23:
            return "Virgo"
        else:
            return "Libra"
    elif month == 10:
        if day <= 23:
            return "Libra"
        else:
            return "Scorpio"
    elif month == 11:
        if day <= 22:
            return "Scorpio"
        else:
            return "Sagittarius"
    elif month == 12:
        if day <= 21:
            return "Sagittarius"
        else:
            return "Capricorn"
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
