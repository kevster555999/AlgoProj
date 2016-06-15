from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Data


def index(request):
    return render(request,'index.html')

def user(request, username):
    return HttpResponse("Hello World from: %s." % username)

