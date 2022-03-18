from turtle import pd
from django.shortcuts import render


def auth(request):
    return render(request, 'home.html')


def profile(request):
    import pdb; pdb.set_trace()
    
