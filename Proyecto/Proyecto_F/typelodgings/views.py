from django.shortcuts import render, redirect
from typelodgings.models import Typelodging
from .forms import TypelodgingsForm

def typelodgings(request):    
    Typelodgings_list = Typelodging.objects.all()    
    return render(request, 'typelodgings/index.html', {'typelodgings_list': Typelodgings_list})

def change_status_typelodging(request, typelodging_idid):
    typelodging= Typelodging.objects.get(pk=typelodging_id)
    typelodging.status = not typelodging.status
    typelodging.save()
    return redirect('typelodgings')

def create_typelodging(request):
    form = TypelodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('typelodgings')    
    return render(request, 'typelodgings/create.html', {'form': form})

