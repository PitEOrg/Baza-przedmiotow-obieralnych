# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours', models.IntegerField()),
                ('Instructor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Class_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('MinStudents', models.IntegerField()),
                ('MaxStudents', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('ID_NO', models.IntegerField()),
                ('ECTS', models.IntegerField()),
                ('Desription', models.TextField()),
                ('Hours', models.IntegerField()),
                ('MinStudents', models.IntegerField()),
                ('MaxStudents', models.IntegerField()),
                ('Semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.TextField()),
                ('Title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FieldOfStudy', models.TextField()),
                ('Year_2', models.IntegerField()),
                ('Semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_has_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_Class_Type_idClass', models.ForeignKey(to='obieraki.Class_Type')),
                ('Class_Course_idCourse', models.ForeignKey(to='obieraki.Course')),
                ('Student_idStudent', models.ForeignKey(to='obieraki.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_has_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_idCourse', models.ForeignKey(to='obieraki.Course')),
                ('Student_idStudent', models.ForeignKey(to='obieraki.Student')),
            ],
        ),
        migrations.CreateModel(
            name='User_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Surname', models.TextField()),
                ('Mail', models.TextField(unique=True)),
                ('Login', models.TextField(unique=True)),
                ('Password_2', models.TextField()),
                ('Permission', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='User_2_idUser_2',
            field=models.ForeignKey(to='obieraki.User_2'),
        ),
        migrations.AddField(
            model_name='staff',
            name='User_2_idUser_2',
            field=models.ForeignKey(to='obieraki.User_2'),
        ),
        migrations.AddField(
            model_name='course',
            name='Staff_idStaff',
            field=models.ForeignKey(to='obieraki.User_2'),
        ),
        migrations.AddField(
            model_name='class',
            name='Class_Type_idClass',
            field=models.ForeignKey(to='obieraki.Class_Type'),
        ),
        migrations.AddField(
            model_name='class',
            name='Course_idCourse',
            field=models.ForeignKey(to='obieraki.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='Staff_idStaff',
            field=models.ForeignKey(to='obieraki.Staff'),
        ),
    ]
