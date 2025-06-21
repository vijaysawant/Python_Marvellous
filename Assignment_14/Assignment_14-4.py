"""
4. Create a class Student with name, roll_no, and a class variable school_name.
Print student details and school name. Change the school name using class name.
"""


class Student:
    schoolName = None
    def __init__(self,s_name, r_no, school_name):
        self.student_name = s_name
        self.roll_no = r_no
        Student.schoolName = school_name

    def display(self):
        print("Student Name: ",self.student_name)
        print("Student Roll No: ",self.roll_no)
        print("School Name : ",Student.schoolName)

def main():
    stud_Obj = Student(s_name="Ramesh",r_no=11, school_name="ABC School")
    stud_Obj.display()
    print("Updating school name")
    stud_Obj.__class__.schoolName = "PQR School"
    stud_Obj.display()

if __name__ == "__main__":
    main()
