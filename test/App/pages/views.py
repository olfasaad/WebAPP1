from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Login
from .Form import Loginn ,LoginForm
# Create your views here.

def index(request):
    username=request.POST.get('user')
   
    email=request.POST.get('email')
    pwd=request.POST.get('password')
    data=Login(username=username,email=email,password=pwd)
    data.save()
    return render(request,'Form/form.html',{'username':username})
def form2(request):
     username=request.POST.get('user')
     pwd=request.POST.get('password')
     data=Login(username=username,password=pwd)
     data.save()
     return render(request,'Form/form2.html',{'lf':Loginn,'username':username},)
def form3(request):

    return render(request,'Form/form3.html',{'lf':LoginForm})

def f1(request):
   return render(request,'pages/index.html',{'name':'olfa saad foufa saad','age':25,'prenom':'','number':256255314856})

def about (request):
    return render (request,'pages/about.html')