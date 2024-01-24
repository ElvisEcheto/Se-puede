from django.shortcuts import render, redirect
from servicepacks.models import Servicepack
from .forms import ServicepackForm

def servicepacks(request):    
    servicepacks_list = Servicepack.objects.all()    
    return render(request, 'servicepacks/index.html', {'servicepacks_list': servicepacks_list})

def change_status_servicepack(request, servicepack_id):
    servicepack= Servicepack.objects.get(pk=servicepack_id)
    servicepack.status = not servicepack.status
    servicepack.save()
    return redirect('servicepacks')

def create_servicepack(request):
    form = ServicepackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('servicepacks')    
    return render(request, 'servicepacks/create.html', {'form': form})