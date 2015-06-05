from django.contrib import admin
from .models import *

#admin.site.register(User_2)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Class_Type)
admin.site.register(Student_has_Course)
admin.site.register(Student_has_Class)

# Register your models here.
