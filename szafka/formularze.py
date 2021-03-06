from django import forms
from .models import Szafka

class SzafkaForm(forms.Form):

    nazwa       = forms.CharField (max_length=300)
    szerokosc   = forms.IntegerField()
    wysokosc    = forms.IntegerField()
    glebokosc   = forms.IntegerField()
    plyta       = forms.IntegerField()

    class meta:
        model = Szafka
        
