from django.shortcuts import render
from .models import *
# Create your views here.


def Home(request):
    return render(request, 'home.html')


def Usecases(request):
    Food = Usecase.objects.filter(category='F')
    Pharmaceutical_Bio = Usecase.objects.filter(category='PB')
    Precision_machine = Usecase.objects.filter(category='PM')
    Electronics_industry = Usecase.objects.filter(category='EL')
    Facility_management = Usecase.objects.filter(category='FM')
    Water_treatment = Usecase.objects.filter(category='WT')
    Smart_Farm = Usecase.objects.filter(category='SF')
    Oem = Usecase.objects.filter(category='O')
    return render(request, 'usecase.html',{  'Food': Food,
        'Pharmaceutical_Bio': Pharmaceutical_Bio,
        'Precision_machine': Precision_machine,
        'Electronics_industry': Electronics_industry,
        'Facility_management': Facility_management,
        'Water_treatment': Water_treatment,
        'Smart_Farm': Smart_Farm,
        'Oem': Oem,
     })


def Products(request):
    Network = Product.objects.filter(category='N')
    return render(request, 'products.html',{
        'Network': Network
    })


def About(request):
    return render(request , 'about.html')

def Productdetails(request,pk):
    product = Product.objects.get(pk=pk)

    return render(request , 'productdetails.html', {'product': product})