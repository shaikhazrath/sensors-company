from django.shortcuts import render
from .models import *
# Create your views here.


def Home(request):
    return render(request, 'home.html')


def Usecases(request,pk):

    usecase = Usecase.objects.filter(category=pk)
    return render(request, 'usecase.html',{  'usecase': usecase,
     })


def Products(request,pk):
    print(pk)
    Network = Product.objects.filter(category=pk)
    return render(request, 'products.html',{
        'Network': Network
    })


def About(request):
    return render(request , 'about.html')

def Productdetails(request,pk):

    product = Product.objects.get(pk=pk)

    return render(request , 'productdetails.html', {'product': product})


def Contact(request):
    return render(request , 'contact.html')