from django.shortcuts import render
from django.http import HttpResponse
from .models import person,issue

# Create your views here.


def max(request):
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "message":'this is redirecting to another'
    }
    return render(request, "home.html",context)

def index(request):
  mymembers = person.objects.all().values()
  context = {
    'mymembers': mymembers,
  }
  

  return render(request,'index.html',context)




def person_list(request):
  mymembers = person.objects.all().values()
  context = {
    'mymembers': mymembers,
  }
  

  return render(request,'home.html',context)


def peak(request):
  mymembers = issue.objects.all().values()
  context = {
    'mymembers': mymembers,
  }
  

  return render(request,'image.html',context)



def add(request):
  method= issue.objects.all().values()
  context = {
    'method': method,
  }
  
  return render(request,'crack.html',context)


def sub(request):
  return render(request,'ground.html' )

