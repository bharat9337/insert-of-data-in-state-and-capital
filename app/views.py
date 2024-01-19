from django.shortcuts import render

from app.forms import *

from django.http import HttpResponse

# Create your views here.

def insert_state(request):

    ESFO=Stateform()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=Stateform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('INSERT STATE SUCCESSFULLY:::')

    return render(request,'insert_state.html',d)



def insert_capital(request):

    ECFO=Capitalform()
    d={'ECFO':ECFO}

    if request.method=='POST':
        CFDO=Capitalform(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('INSERT CAPITAL SUCCESSFULLY:::')

    return render(request,'insert_capital.html',d)