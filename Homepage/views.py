from django.shortcuts import render, redirect
from .models import Home, Testify
from .forms import TestimonyForm
from django.contrib import messages

# Create your views here.
def index(request):
    home_view = Home.objects.all()
    return render(request, 'home.html', {'home_view': home_view})

def testify(request):
    if request.method =='GET':

        testimonies = Testify.objects.all()
   
    if request.method == 'POST':
        data = request.POST.copy()
        Testify.objects.create(
            title=data.get('title'),
            testimony=data.get('testimony'),
        )
        messages.success(request, 'Your testimony about our services has been saved successfully!')
        return redirect('testimonies')
    
    return render(request, 'testimonies.html', {'testimonies': testimonies})

def about(request):

    return render(request, 'about.html')

def price(request):

    return render(request, 'price.html')