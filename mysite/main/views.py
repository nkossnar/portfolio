from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#SERVES HTTP RESQUESTS
def index(response):
    return HttpResponse("haha welcome to my website")

def view1(response):
    return HttpResponse("View1")

def html_template(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())