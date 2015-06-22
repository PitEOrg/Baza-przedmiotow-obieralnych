from django.db import models
from django.contrib.auth.models import User

#Create your models here.
# Zakomentowane zostaly elementy ktore przy odbiorze projektu uznano za niepotrzebne
# W razie koniecznosci mozna je przywrocic do dzialania
# TO DO: Mozliwosc stworzenia studenta bez stworzonego jeszcze konta dla niego

    
class Student(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    Mail = models.TextField(max_length=30)						
    FieldOfStudy = models.TextField(max_length=30)				
    Year_2 = models.IntegerField()						
    Semester = models.IntegerField()
    CollectedECTS = models.IntegerField()
    def __str__(self):
        return self.user.first_name.decode("utf-8") + ' ' + self.user.last_name.decode("utf-8")


class Staff(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    Mail = models.TextField(max_length=30)							
    Title = models.TextField(max_length=30)
    Department = models.TextField(max_length=30)
    def __str__(self):
        return self.user.first_name.decode("utf-8") + ' ' + self.user.last_name.decode("utf-8")


class Course(models.Model):
    Name = models.TextField(max_length=30)
    Staff_idStaff = models.ForeignKey(Staff)
    ECTS = models.IntegerField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()
    Semester = models.IntegerField()
    Desription = models.TextField()
    Requirements = models.TextField()
    WayOfGettingCredit = models.TextField()
    Requirements = models.TextField()					
    Exam = models.BooleanField()
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


