from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "AppPrimaria/home.html")

def textos(request):
    return render(request, "AppPrimaria/textos.html")
