from django.shortcuts import *

# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from obieraki.models import Student 
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from obieraki.forms import RegisterForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render



def main_site(request):
	return render(request, 'src/index.html', {})

def account_info(request):
	return render(request, 'src/account_info.html', {})

def courses(request):
	return render(request, 'src/courses.html', {})

def mycourses(request):
	return render(request, 'src/mycourses.html', {})

def logout_page(request):
    logout(request)
    return render(request, "src/index.html", {})

#def register_page(request):
#	if request.method =='POST':
#		form = RegisterForm(request.POST)
#		if form.is_valid():
#			return HttpResponseRedirect("/")
#	else:
#		form = RegisterForm()
#	template = get_template('registration/register.html')
#	var = RequestContext(request, {'form':form})
#	output = template.render(var)
#	return HttpResponse(output)

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/index/")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form,})


