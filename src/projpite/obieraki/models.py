from django.db import models

#Create your models here.

class Class_Type(models.Model):
    Name = models.TextField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()

class User_2(models.Model):
    Name = models.TextField()
    Surname = models.TextField()
    Mail = models.TextField(unique=True)
    Login = models.TextField(unique=True)
    Password_2 = models.TextField()
    Permission = models.IntegerField()
    
    
class Student(models.Model):
    User_2_idUser_2 = models.ForeignKey(User_2)
    FieldOfStudy = models.TextField()
    Year_2 = models.IntegerField()
    Semester = models.IntegerField()

class Staff(models.Model):
    User_2_idUser_2 = models.ForeignKey(User_2)
    Department = models.TextField()
    Title = models.TextField()


class Course(models.Model):
    Staff_idStaff = models.ForeignKey(User_2)
    Name = models.TextField()
    ID_NO = models.IntegerField()
    ECTS = models.IntegerField()
    Desription = models.TextField()
    Hours = models.IntegerField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()
    Semester = models.IntegerField()


class Student_has_Course(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Course_idCourse = models.ForeignKey(Course)


class Class(models.Model):
    Course_idCourse = models.ForeignKey(Course)
    Class_Type_idClass = models.ForeignKey(Class_Type)
    Staff_idStaff = models.ForeignKey(Staff)
    Hours = models.IntegerField()
    Instructor = models.TextField()

class Student_has_Class(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Class_Course_idCourse = models.ForeignKey(Course)
    Class_Class_Type_idClass = models.ForeignKey(Class_Type)
