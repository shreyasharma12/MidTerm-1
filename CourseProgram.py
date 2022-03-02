'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''


import CourseClass as c

def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']


    my_student = c.Course("John",crn,seats,status)
    my_student1 = c.Course("James",crn,seats,status)
    my_student2 = c.Course("Jill",crn,seats,status)
    my_student3 = c.Course("Jack",crn,seats,status)

    print("Student Name:",my_student.get_name())
    print("Course Name: MIS 4322 - Advanced Python")
    print("CRN:",my_student.get_crn())
    print("Seats left:",my_student.get_seats(),"\n")

    print("Student Name:",my_student1.get_name())
    print("Course Name: MIS 4322 - Advanced Python")
    print("CRN:",my_student1.get_crn())
    print("Seats left:",my_student1.get_seats(),"\n")

    print("Student Name:",my_student2.get_name())
    print("Course Name: MIS 4322 - Advanced Python")
    print("CRN:",my_student2.get_crn())
    print("Seats left:",my_student2.get_seats(),"\n")

    print("Student Name:",my_student3.get_name())
    print("Course Name: MIS 4322 - Advanced Python")
    print("CRN:",my_student3.get_crn())
    print("Seats left:",my_student3.get_seats(),"\n")



    if my_student1.get_crn() == my_student.get_crn():
       seats -= my_student1.get_seats()

    if my_student2.get_crn() == my_student1.get_crn():
       seats -= my_student2.get_seats()

    if my_student3.get_crn() == my_student2.get_crn():
       seats -= my_student3.get_seats()
    
    if seats == 0: 
      print("Sorry Joanne, registration is closed for MIS 4322 - Advanced Python")


main()

###################################################################




        
    
    
