"""
URL configuration for coderone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from codeapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about,name='about'),
    path('contact/', views.contact, name='contact'),
    path('bank/', views.bank,name='bankingandfinance'),
    path('service/', views.service,name='service'),
    path('ben/', views.ben,name='ben'),
    path('family/', views.family,name='familylaw'),
    path('will/', views.will,name='wills and probate'),
    path('employ/', views.employ,name='employmentlaw'),
    path('liti/', views.liti,name='litigation'),
    path('rent/',views.rent,name='rentrepayment'),
    path('land/',views.land,name='landlord&tenent'),
    path('clinical/',views.clinical,name='clinicalnegligence'),
    path('contract/',views.contract,name='contract'),
    path('debt/',views.debt,name='debtrecovery'),
    path('hrushi/',views.hrushi,name='hrushi'),
    path('insolve/',views.insolve,name='insolvencymatters'),
    path('ishrat/',views.ishrat,name='ishrat'),
    path('kal/',views.kal,name='kalana'),
    path('team/',views.team,name='team'),
    path('trade/',views.trade,name='tradefinance')
]
