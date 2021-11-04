from django import forms

class SaveForm(forms.Form):
    tempString = forms.CharField(label='tempString', max_length=200)