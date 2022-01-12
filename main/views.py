from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Welcome To cherry homepage")
    return render(request, "home.html")

def about_us(request):
    # return HttpResponse("We sell cherry")
    return render(request, "about.html")

def contact_us(request):
    # return HttpResponse("This is our services")
    return render(request,"contact.html" )