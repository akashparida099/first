from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def snacks(request):
    return HttpResponse('GARLIC MIXTURE')