from django import forms

class CityForm(forms.Form):
    city = forms.CharField(max_length=100)