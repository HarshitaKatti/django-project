from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")
def about(request):
    return HttpResponse("This is the About Page.")
def welcome(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')