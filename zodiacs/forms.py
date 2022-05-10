from django import forms

class BirthdayForm(forms.Form):
    birthday = forms.DateField(label='birthday', widget=forms.SelectDateWidget(years=range(1900, 2025),  attrs={'class': 'form-control'}))
