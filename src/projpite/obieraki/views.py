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
		if request.user.is_superuser:
			return render(request, 'admin/index_admin.html',{'user' : request.user})
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
				courses = (courses for courses in Course.objects.filter(Staff_idStaff = st.id))
				return render(request, 'Staff/mycourses.html', {'staff': st, 'courses': courses})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
		else:
			return render(request, '404.html', {})
	else:
		return render(request, '404.html', {})

def class_add(request, course_id, class_id):
	course = Course.objects.get(pk=course_id)
	class_ = Class.objects.get(pk=class_id)
	class_type = Class_Type.objects.get(pk=class_.Class_Type_idClass.id)
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				try:
					old_course = Student_has_Course.objects.get(Student_idStudent=st, Course_idCourse=course)
				except Student_has_Course.DoesNotExist:
					new_course = Student_has_Course(Student_idStudent=st, Course_idCourse=course)
					new_course.save()
					st.CollectedECTS += course.ECTS
					st.save()
				try:
					old_class = Student_has_Class.objects.get(Student_idStudent=st, Class_Course_idCourse=course, Class_Class_Type_idClass=class_type)
				except Student_has_Class.DoesNotExist:
					new_class = Student_has_Class(Student_idStudent=st, Class_Course_idCourse=course, Class_Class_Type_idClass=class_type)
					new_class.save()
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		else:
			return render(request, '404.html', {})
	else:
		return render(request, '404.html', {})

def class_remove(request, course_id, class_id):
	course = Course.objects.get(pk=course_id)
	class_ = Class.objects.get(pk=class_id)
	class_type = Class_Type.objects.get(pk=class_.Class_Type_idClass.id)
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				try:
					old_class = Student_has_Class.objects.get(Student_idStudent=st, Class_Course_idCourse=course, Class_Class_Type_idClass=class_type)
					old_class.delete()
					try:
						other_classes = Student_has_Class.objects.get(Student_idStudent=st, Class_Course_idCourse=course)
					except Student_has_Class.MultipleObjectsReturned:
						other_classes = []
					except Student_has_Class.DoesNotExist:
						try:
							old_course = Student_has_Course.objects.get(Student_idStudent=st, Course_idCourse=course)
							old_course.delete()
							st.CollectedECTS -= course.ECTS
							st.save()
						except Student_has_Course.DoesNotExist:
							new_course = Student_has_Course(Student_idStudent=st, Course_idCourse=course)
				except Student_has_Class.DoesNotExist:
					new_class = Student_has_Class(Student_idStudent=st, Class_Course_idCourse=course, Class_Class_Type_idClass=class_type)
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		else:
			return render(request, '404.html', {})
	else:
		return render(request, '404.html', {})

def mycourse_info(request, course_id):
	course = Course.objects.get(pk=course_id)
	if request.user.is_authenticated():
		if request.user.groups.filter(name='Student').exists():
			try:
				st = Student.objects.get(user=request.user)
				classes_types = (has_classes.Class_Class_Type_idClass for has_classes in Student_has_Class.objects.filter(Student_idStudent=st, Class_Course_idCourse = course))
				classes = Class.objects.all()
				chosen_classes = []
				for i in classes_types:
					new_class = Class.objects.get(Class_Type_idClass = i, Course_idCourse = course_id)
					chosen_classes.append(new_class.id)
				classes = classes.filter(pk__in=chosen_classes)
				return render(request, 'Student/course_info.html', {'student': st, 'course': course, 'classes': classes})
			except Student.DoesNotExist:
				return render(request, '404.html', {})
		elif	request.user.groups.filter(name='Staff').exists():
			try:
				st = Staff.objects.get(user=request.user)
				classes = (classes for classes in Class.objects.filter(Course_idCourse = course_id))
				if request.method == 'POST':
					course.Description = request.POST['Description']
					course.Requirements = request.POST['Requirements']
					course.WayOfGettingCredit = request.POST['WayOfGettingCredit']
					course.save()
				return render(request, 'Staff/course_info.html', {'staff': st, 'course': course, 'classes': classes})
			except Staff.DoesNotExist:
				return render(request, '404.html', {})
	else:
		classes = (classes for classes in Class.objects.filter(Course_idCourse = course_id))
		return render(request, 'course_info.html', {'course': course, 'classes': classes})

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
				if request.method == 'POST':
					course.Description = request.POST['Description']
					course.Requirements = request.POST['Requirements']
					course.WayOfGettingCredit = request.POST['WayOfGettingCredit']
					course.save()
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
	if not request.user.is_superuser:
		return render(request, '404.html', {})

	if request.method == 'POST':

		form = ClassForm(request.POST)
		if form.is_valid():
			new_object= form.save()
			return HttpResponseRedirect("/")
		form = StudentForm(request.POST)
		if form.is_valid():
			new_object= form.save()
			your_user = request.POST['user']
			g = Group.objects.get(name='Student')
			g.user_set.add(your_user)
			return HttpResponseRedirect("/")
		form = StaffForm(request.POST)
		if form.is_valid():
			new_object= form.save()
			your_user = request.POST['user']
			g = Group.objects.get(name='Staff')
			g.user_set.add(your_user)
			return HttpResponseRedirect("/")
		form = CourseForm(request.POST)
		if form.is_valid():
			new_object= form.save()
			return HttpResponseRedirect("/")
		form = ChooseForm(request.POST)
		if form.is_valid():
			mhm = request.POST['Dodaj']
			form = formFactory(mhm)
	else:
		form = ChooseForm()
	return render(request, 'admin/add.html', {'form': form, 'user':request.user})





def delete(request):
	
	if request.method == 'POST':
		form = YourForm(request.POST)
		if form.is_valid():

			instance = Student.objects.get(id=request.POST['field1'])
			instance.delete()
	formStudent = DeleteStudentForm
	formClass = DeleteClassForm
	formStaff = DeleteStaffForm
	formCourse = DeleteCourseForm
	return render(request, 'admin/remove.html', {'formStudent': formStudent,'formClass': formClass,'formStaff': formStaff,'formCourse': formCourse  })



def deleteStudent(request):
	
	if request.method == 'POST':
		form = DeleteStudentForm(request.POST)
		if form.is_valid():
			instance = Student.objects.get(id=request.POST['student'])
			instance.delete()
			return HttpResponseRedirect("/delete/")
	
	return HttpResponseRedirect("/")

def deleteClass(request):
	
	if request.method == 'POST':
		form = DeleteClassForm(request.POST)
		if form.is_valid():
			instance = Class.objects.get(id=request.POST['classOb'])
			instance.delete()
			return HttpResponseRedirect("/delete/")
	
	return HttpResponseRedirect("/")

def deleteStaff(request):
	
	if request.method == 'POST':
		form = DeleteStaffForm(request.POST)
		if form.is_valid():
			instance = Staff.objects.get(id=request.POST['staff'])
			instance.delete()
			return HttpResponseRedirect("/delete/")
	
	return HttpResponseRedirect("/")

def deleteCourse(request):
	
	if request.method == 'POST':
		form = DeleteCourseForm(request.POST)
		if form.is_valid():
			instance = Course.objects.get(id=request.POST['course'])
			instance.delete()
			return HttpResponseRedirect("/delete/")
	
	return HttpResponseRedirect("/")
