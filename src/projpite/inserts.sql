INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Admin', 'Admin', 'admin@agh.edu.pl', 'admin', 'admin', 99);
INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Juliusz', 'Trabka', 'trabka@agh.edu.pl', 'student1', 'student1', 1);
INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Maciej', 'Lit', 'lit@agh.edu.pl', 'student2', 'student2', 1);
INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Mateusz', 'Molibdenowy', 'molibdenowy@agh.edu.pl', 'staff1', 'staff1', 2);
INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Janusz', 'Tytanowy', 'tytanowy@agh.edu.pl', 'staff2', 'staff2', 2);
INSERT INTO obieraki_user_2(Name , Surname, Mail, Login, Password_2, Permission) 
        VALUES ('Tadeusz', 'Wolframowy', 'wolframowy@agh.edu.pl', 'staff3', 'staff3', 2);


INSERT INTO obieraki_class_type(Name, MinStudents, MaxStudents) VALUES ('Lecture', 7, 150);
INSERT INTO obieraki_class_type(Name, MinStudents, MaxStudents) VALUES ('Laboratory class', 7, 15);
INSERT INTO obieraki_class_type(Name, MinStudents, MaxStudents) VALUES ('Class', 10, 30);
INSERT INTO obieraki_class_type(Name, MinStudents, MaxStudents) VALUES ('Seminar', 7, 20);
INSERT INTO obieraki_class_type(Name, MinStudents, MaxStudents) VALUES ('Project class', 7, 15);


INSERT INTO obieraki_student(User_2_idUser_2_id, FieldOfStudy, Year_2, Semester, ID) VALUES (2, 'Applied Computer Science', 2, 3, 1222);
INSERT INTO obieraki_student(User_2_idUser_2_id, FieldOfStudy, Year_2, Semester, ID) VALUES (3, 'Theoretical Physics', 4, 7, 2222);

INSERT INTO obieraki_staff(User_2_idUser_2_id, Department, Title) VALUES (4, 'Department of Computer Science', 'Ph.D');
INSERT INTO obieraki_staff(User_2_idUser_2_id, Department, Title) VALUES (5, 'Department of Theoretical Physics', 'D.Sc');
INSERT INTO obieraki_staff(User_2_idUser_2_id, Department, Title) VALUES (6, 'Department of Computer Science', 'B.Sc');


INSERT INTO obieraki_course(Staff_idStaff_id, Name, ID_NO, ECTS, Desription, Hours, MinStudents, MaxStudents, Semester) 
        VALUES (1, 'Quantum Physics', 101, 8, 'Quantum Physics - Course description', 120, 15, 60, 0);
INSERT INTO obieraki_course(Staff_idStaff_id, Name, ID_NO, ECTS, Desription, Hours, MinStudents, MaxStudents, Semester) 
        VALUES (2, 'Introduction to databases', 102, 4, 'Introduction to databases - Course description', 60, 15, 30, 1);


INSERT INTO obieraki_student_has_course(Student_idStudent_id, Course_idCourse_id) VALUES (1, 1);
INSERT INTO obieraki_student_has_course(Student_idStudent_id, Course_idCourse_id) VALUES (1, 2);
INSERT INTO obieraki_student_has_Course(Student_idStudent_id, Course_idCourse_id) VALUES (2, 1);


INSERT INTO obieraki_class(Course_idCourse_id, Class_Type_idClass_id, Staff_idStaff_id, Hours, Instructor) VALUES (1, 1, 2, 60, 'D.Sc. Prof2');
INSERT INTO obieraki_class(Course_idCourse_id, Class_Type_idClass_id, Staff_idStaff_id, Hours, Instructor) VALUES (1, 3, 2, 30, 'D.Sc. Prof2');
INSERT INTO obieraki_class(Course_idCourse_id, Class_Type_idClass_id, Staff_idStaff_id, Hours, Instructor) VALUES (1, 2, 1, 30, 'Ph.D. Prof1');
INSERT INTO obieraki_class(Course_idCourse_id, Class_Type_idClass_id, Staff_idStaff_id, Hours, Instructor) VALUES (2, 1, 1, 30, 'Ph.D. Prof1');
INSERT INTO obieraki_class(Course_idCourse_id, Class_Type_idClass_id, Staff_idStaff_id, Hours, Instructor) VALUES (2, 2, 1, 30, 'Ph.D. Prof1');


INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (1, 1, 1);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (1, 1, 2);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (1, 1, 3);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (2, 1, 1);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (2, 1, 2);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (2, 1, 3);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (1, 2, 1);
INSERT INTO obieraki_student_has_class(Student_idStudent_id, Class_Course_idCourse_id, Class_Class_Type_idClass_id) VALUES (1, 2, 2);