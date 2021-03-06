from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .formularze import SzafkaForm
from .models import Szafka

class boki:
    y=0
    z=0
    okleina="Okleina"
class dol:
    x=0
    z=0
    okleina="Okleina"
class gora:
    x=0
    z=0
    okleina="Okleina"
class front:
    x=0
    y=0
    okleina="Okleina"


def szafka_rozpisana_view(request,id):

    obj = Szafka.objects.get(id = id)
    boki_s = boki()
    boki_s.y = obj.wysokosc - obj.plyta 
    boki_s.z = obj.glebokosc

    dol_s = dol()
    dol_s.x =obj.szerokosc
    dol_s.z =obj.glebokosc
    
    gora_s = gora()
    gora_s.x =obj.szerokosc - 2*obj.plyta
    gora_s.z =obj.glebokosc

    front_s = front()
    front_s.x =obj.szerokosc - 2*obj.plyta
    front_s.y =obj.wysokosc - 2*obj.plyta

    context = {
        'szafka':obj,
        'boki':boki_s,
        'dol':dol_s,
        'gora':gora_s,
        'front':front_s,
    }
    return render (request, "rozpisana.html", context)


def szafka_create_view(request,*args,**kwargs):

    d_nowa = SzafkaForm()
    if request.method == 'POST':
        d_nowa = SzafkaForm(request.POST)
        if d_nowa.is_valid():
             new = Szafka.objects.create(**d_nowa.cleaned_data)
             path= "../szafka/"+str(new.id)
             return redirect(path)
        else:
             print(d_nowa.errors)


    context = {
       'form': d_nowa
    }

    return render (request, "create_view.html", context)
# Create your views here.
