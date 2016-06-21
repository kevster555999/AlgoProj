from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Data


def index(request):
    return render(request,'index.html')

def log_in(request):
    return render(request,'login.html')

def analytics(request):
    return render(request,'analytics.html')


def contact(request):
    x = "Name: Kevin Huang \nEmail: kh522@cornell.edu"
    return HttpResponse(x)

def projects(request):
    return HttpResponse("Projects will go here")


def user(request, username):
    return HttpResponse("Invalid Link: %s." % username)

