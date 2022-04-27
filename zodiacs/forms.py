from django import forms

# from .models import Sign

class BirthForm(forms.Form):
    birth_field = forms.DateField(input_formats=['%d/%m/%Y'])
    
    # class Meta:
    #     model = None
    #     fields = ['text']
    #     labels = {'text': 'label'}