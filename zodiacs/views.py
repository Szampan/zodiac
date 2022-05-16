# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import FormView             

from .models import Sign
from .tools import *
from .forms import BirthdayForm
           

class IndexFormView(FormView):
    model = Sign
    form_class = BirthdayForm
    template_name = 'zodiacs/index.html'
    success_url = '/'                           # reverse_lazy?

    def form_valid(self, form, **kwargs): 
        context = self.get_context_data(**kwargs)
        sign = get_sign(form.cleaned_data['birthday'])
        try:
            context['db_sign'] = Sign.objects.get(name=sign)
        except:
            print('No such sign in DB')         # to do: error handling
        return super().render_to_response(context)
        # return super().form_valid(form)       # default


        