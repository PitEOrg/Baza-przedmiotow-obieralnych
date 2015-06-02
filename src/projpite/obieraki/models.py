from django.db import models

#Create your models here.
# Zakomentowane zostały elementy które przy odbiorze projektu uznano za niepotrzebne
# W razie konieczności można je przywrócić do działania

class Class_Type(models.Model):
    Name = models.TextField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()


class User_2(models.Model):
    Login = models.TextField(unique=True)
    Password_2 = models.TextField()
    Mail = models.TextField(unique=True)
    Permission = models.IntegerField()
    #Name = models.TextField()
    #Surname = models.TextField()
    
    
class Student(models.Model):
    User_2_idUser_2 = models.ForeignKey(User_2)
    Name = models.TextField()
    Surname = models.TextField()
    FieldOfStudy = models.TextField()
    Year_2 = models.IntegerField()
    Semester = models.IntegerField()
    CollectedECTS = models.IntegerField()


class Staff(models.Model):
    User_2_idUser_2 = models.ForeignKey(User_2)
    Name = models.TextField()
    Surname = models.TextField()
    Title = models.TextField()
    Department = models.TextField()


class Course(models.Model):
    Name = models.TextField()
    Staff_idStaff = models.ForeignKey(User_2)
    ECTS = models.IntegerField()
    MinStudents = models.IntegerField()
    MaxStudents = models.IntegerField()
    Semester = models.IntegerField()
    Desription = models.TextField()
    Requirements = models.TextField()
    WayOfGettingCredit = models.TextField()
    Requirements = models.TextField()
    Exam = models.BooleanField()
    #Hours = models.IntegerField()
    #ID_NO = models.IntegerField()


class Class(models.Model):
    Course_idCourse = models.ForeignKey(Course)
    Class_Type_idClass = models.ForeignKey(Class_Type)
    Staff_idStaff = models.ForeignKey(Staff)
    Hours = models.IntegerField()
    #Instructor = models.TextField()


class Student_has_Course(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Course_idCourse = models.ForeignKey(Course)


class Student_has_Class(models.Model):
    Student_idStudent = models.ForeignKey(Student)
    Class_Course_idCourse = models.ForeignKey(Course)
    Class_Class_Type_idClass = models.ForeignKey(Class_Type)


