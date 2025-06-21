"""
1. Create a class Employee with attributes name, emp_id and salary. Create objects of this class and print their details using
a method.
Expected Output:
Name: Rohit, ID: 101, Salary: 50000
"""

class Employee:
    def __init__(self, name, id, sal):
        self.name = name
        self.emp_id = id
        self.salary = sal

    def DisplayEmployeDetails(self):
        print("Name: ",self.name)
        print("ID: ",self.emp_id)
        print("Salary: ",self.salary)

def main():
    empObj = Employee("Rohit",101, 50000)
    empObj.DisplayEmployeDetails()

if __name__ == "__main__":
    main()