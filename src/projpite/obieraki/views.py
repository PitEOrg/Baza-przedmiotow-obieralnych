from django.shortcuts import *

# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from obieraki.models import *
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from obieraki.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

def main_site(request):
	if request.user.is_authenticated():
		if request.user.username == 'admin':
			form = ChooseForm()
			return render(request, 'admin/index_admin.html',{})

		elif request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				return render(request, 'Student/index_student.html', {'student': st})
			except Student.DoesNotExist:
				return render(request, 'Student/index_student_no_acc.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				return render(request, 'Staff/index_staff.html', {'staff': st})
			except Staff.DoesNotExist:
				return render(request, 'Staff/index_staff_no_acc.html', {})
		else:
			return render(request, 'no_acc/index_no_acc.html', {})
	else:
		return render(request, 'index.html', {})

def account_info(request):
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				return render(request, 'Student/account_info.html', {'student': st})
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				return render(request, 'Staff/account_info.html', {'staff': st})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
	else:
		return render(request, '404.html', {})

def courses(request):
	courses = Course.objects.all()
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				return render(request, 'Student/courses.html', {'student': st, 'courses': courses})
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				return render(request, 'Staff/courses.html', {'staff': st, 'courses': courses})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
	else:
		return render(request, 'courses.html', {'courses': courses})

def mycourses(request):
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				courses = (courses.Course_idCourse for courses in Student_has_Course.objects.filter(Student_idStudent = st.id))
				return render(request, 'Student/mycourses.html', {'student': st, 'courses': courses})
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				return render(request, 'Staff/mycourses.html', {'staff': st})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
	else:
		return render(request, '404.html', {})

def course_info(request, course_id):
	course = Course.objects.get(pk=course_id)
	classes = (classes for classes in Class.objects.filter(Course_idCourse = course_id))
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				return render(request, 'Student/course_info.html', {'student': st, 'course': course, 'classes': classes})
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				return render(request, 'Staff/course_info.html', {'staff': st, 'course': course, 'classes': classes})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
	else:
		return render(request, 'course_info.html', {'course': course, 'classes': classes})

def logout_page(request):
    logout(request)
    return render(request, 'index.html', {})

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            try:
                st = Student.objects.get(Mail=new_user.email)
                g = Group.objects.get(name='Student') 
                g.user_set.add(new_user)
            except Student.DoesNotExist:
                try:
                    te = Staff.objects.get(Mail=new_user.email)
                    g = Group.objects.get(name='Staff') 
                    g.user_set.add(new_user)
                except Staff.DoesNotExist:
                    return HttpResponse("Zly mail")
            return HttpResponseRedirect("/index/")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form,})


def add(request):
	if request.method == 'POST':
		form = ClassForm(request.POST)
		if form.is_valid():
			new_course= form.save()
			return HttpResponseRedirect("/")







		else:
			form = ChooseForm(request.POST)
			if form.is_valid():
				mhm = request.POST['Dodaj']
				form = formFactory(mhm)
	else:
		form = ChooseForm()
	return render(request, 'admin/add.html', {'form': form})


"""
	form = CourseForm(request.POST)
        	if form.is_valid():
            		cd = form.cleaned_data
            		f = CourseForm(request.POST)
            		new_course= f.save()
            		return HttpResponseRedirect("/")

"""