from django import forms
from django.forms import ModelForm      
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm     
from obieraki.models import *


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Login:", max_length=30)
    password1 = forms.CharField(label="Haslo:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtorz haslo:", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email:", required = True)
    name = forms.CharField(label="Imie:", required = True)
    surname = forms.CharField(label="Nazwisko:", required = True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']

        if commit:
            user.save()

        return user




class ParentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentForm(ParentForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(ParentForm):
    class Meta:
        model = Course
        fields = '__all__'

class StaffForm(ParentForm):
    class Meta:
        model = Staff
        fields = '__all__'

class ClassForm(ParentForm):
    class Meta:
        model = Class
        fields = '__all__'


class YourForm(forms.Form):
    field1 = forms.ModelChoiceField(queryset = Student.objects.all(), initial=0 )

class ChooseForm(forms.Form):
        OPTIONS = (
                ("STU", "Student"),
                ("STA", "Staff"),
                ("COU", "Course"),
                ("CLA", "Class"),
                )
        Dodaj = forms.ChoiceField(widget=forms.Select,
                                             choices=OPTIONS)






def formFactory(mhm):
    if mhm == "STU":
        return StudentForm()
    if mhm == "STA":
        return StaffForm()
    if mhm == "COU":
        return CourseForm()
    if mhm == "CLA":
        return ClassForm()
