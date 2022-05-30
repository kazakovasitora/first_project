from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hello_world(request):
    return HttpResponse('Salom Dunyo!')

def Bizning_Jamoa(request):
    return HttpResponse('<h1>Assaomu alaykum siz bizning jamoa bilan tanishasiz!</h1>')