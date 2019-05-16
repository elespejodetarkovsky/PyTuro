# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

# def portfolio(request):
#     return render(request, "core/portfolio.html")

def coockie(request):
    return render(request, "core/coockie.html")

def contact(request):
    return render(request, "core/contact.html")