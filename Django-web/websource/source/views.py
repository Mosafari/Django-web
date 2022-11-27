from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def resolpi(request):
    template = loader.get_template('resourcelpi.html')
    return HttpResponse(template.render())