from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import staff

def demo(request):
    obj=place.objects.all()
    ob=staff.objects.all()


    return render(request, "index.html",{'result':obj,'res':ob})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
# def demo(request):
#     ob=staff.objects.all()
#     return render(request,"index.html",{'res':ob})