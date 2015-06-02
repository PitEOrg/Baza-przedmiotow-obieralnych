from django.shortcuts import *

# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from obieraki.models import Student 
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from obieraki.forms import RegisterForm



def main_site(request):
	return render(request, 'src/index.html', {})

def logout_page(request):
    logout(request)
    return render(request, "src/index.html", {})

def user_information(request):
    return render(request, "src/user_information.html", {})

def register_page(request):
	if request.method =='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/")
	else:
		form = RegisterForm()
	template = get_template('registration/register.html')
	var = RequestContext(request, {'form':form})
	output = template.render(var)
	return HttpResponse(output)


