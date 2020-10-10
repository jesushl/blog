from django.shortcuts import render
from django.template import Context

def index(request):
    context = {'is_blog': True}
    return  render(request, 'index.html', context)
