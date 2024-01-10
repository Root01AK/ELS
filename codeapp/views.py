from operator import index
from django.shortcuts import render
from django.http import HttpResponse
from .models import contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

#about
def about(request):
    return render(request, 'about.html')

#contact
def contact(request):
    return render(request, 'contact.html')

#banking&finance
def bank(request):
    return render(request, 'bankingandfinance.html')

#ben
def ben(request):
    return render(request, 'ben.html')

#clinicalnegligence
def clinical(request):
    return render(request, 'clinicalnegligence.html')

#contract
def contract(request):
    return render(request, 'contract.html')

#debtrecovery
def debt(request):
    return render(request, 'debtrecovery.html')

#employmentlaw
def employ(request):
    return render(request, 'employmentlaw.html')

#familylaw
def family(request):
    return render(request, 'familylaw.html')

#Hurshi
def hrushi(request):
    return render(request, 'hrushi.html')

#insolvencymatters
def insolve(request):
    return render(request, 'insolvencymatters.html')

#Ishrat
def ishrat(request):
    return render(request, 'ishrat.html')

#kalana
def kal(request):
    return render(request, 'kalana.html')

#kareena ---aveni
#def (request):
#return render

#Landlord
def land(request):
    return render(request, 'landlord&tenent.html')

#litigation
def liti(request):
    return render(request, 'litigation.html')

#Rent
def rent(request):
    return render(request, 'rentrepayment.html')

#Services
def service(request):
    return render(request, 'service.html')

#team
def team(request):
    return render(request, 'team.html')

#trade
def trade(request):
    return render(request, 'tradefinance.html')

#wills and probate
def will(request):
    return render(request, 'wills and probate.html')

