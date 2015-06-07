from django.db import models
from django.contrib.auth.models import User

#Create your models here.
# Zakomentowane zostaly elementy ktore przy odbiorze projektu uznano za niepotrzebne
# W razie koniecznosci mozna je przywrocic do dzialania
# TO DO: Mozliwosc stworzenia studenta bez stworzonego jeszcze konta dla niego

class User_2(models.Model): 							#delete
    Login = models.TextField(unique=True)				#delete
    Password_2 = models.TextField()					#delete
    Mail = models.TextField(unique=True)				#delete
    Permission = models.IntegerField()					#delete
    #Name = models.TextField()						#delete
    #Surname = models.TextField()						#delete
    def __str__(self):								#delete
        return self.Mail								#delete
    
    
class Student(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    #User_2_idUser_2 = models.ForeignKey(User_2)
    Name = models.TextField()
    Surname = models.TextField()
    Mail = models.TextField()							#unique
    FieldOfStudy = models.TextField()					#add wydzial
    Year_2 = models.IntegerField()						#zmiana nazwy
    Semester = models.IntegerField()
    CollectedECTS = models.IntegerField()
    def __str__(self):
        return self.Name + ' ' + self.Surname


class Staff(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    #User_2_idUser_2 = models.ForeignKey(User_2)
    Name = models.TextField()
    Surname = models.TextField()
    Mail = models.TextField()							#unique
    Title = models.TextField()
    Department = models.TextField()
    def __str__(self):
        return self.Name + ' ' + self.Surname


class Course(models.Model):
    Name = models.TextField()
    Staff_idStaff = models.ForeignKey(Staff)
    ECTS = models.IntegerField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()
    Semester = models.IntegerField()
    Desription = models.TextField()
    Requirements = models.TextField()
    WayOfGettingCredit = models.TextField()
    Requirements = models.TextField()					#delete
    Exam = models.BooleanField()
    #Hours = models.IntegerField()
    #ID_NO = models.IntegerField()
    def __str__(self):
        return self.Name


class Class_Type(models.Model):
    Name = models.TextField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()
    def __str__(self):
        return self.Name


class Class(models.Model):
    Course_idCourse = models.ForeignKey(Course)
    Class_Type_idClass = models.ForeignKey(Class_Type)
    Staff_idStaff = models.ForeignKey(Staff)
    Hours = models.IntegerField()
    #Instructor = models.TextField()
    def __str__(self):
        return self.Course_idCourse.Name + ' - ' + self.Class_Type_idClass.Name


class Student_has_Course(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Course_idCourse = models.ForeignKey(Course)
    def __str__(self):
        return self.Student_idStudent.Name + ' ' + self.Student_idStudent.Surname + ' - ' + self.Course_idCourse.Name


class Student_has_Class(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Class_Course_idCourse = models.ForeignKey(Course)
    Class_Class_Type_idClass = models.ForeignKey(Class_Type)
    def __str__(self):
        return self.Student_idStudent.Name + ' ' + self.Student_idStudent.Surname + ' - ' + self.Class_Course_idCourse.Name + ' - ' + self.Class_Class_Type_idClass.Name


