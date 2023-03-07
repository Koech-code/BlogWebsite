from django import forms

class TestimonyForm(forms.Form):
    title = forms.CharField(max_length=100)
    testimony = forms.CharField(max_length=100)