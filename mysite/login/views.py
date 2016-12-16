from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Data
from .forms import login_form


def index(request):
	if request.method == 'POST':
		form = login_form(request.POST)
		if form.is_valid():
			user = User(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
			user.save()
			return HttpResponse("Your response has been recorder: %s" % form.cleaned_data['username'])	
	else:
		form = login_form()

	user_list = User.objects.all()
	my_context = { 'user': user_list }
	return render(request,'index.html',my_context)

def log_in(request):
    return render(request,'login.html')

def analytics(request):
    return render(request,'analytics.html')


def contact(request):
	return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')


def user(request, username):
    return HttpResponse("Invalid Link: %s." % username)

