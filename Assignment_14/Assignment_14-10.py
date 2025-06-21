"""
10. Demonstrate private, protected and public access modifiers using a class Employee 
with attributes: __salary, _department, name.
"""

class Employee:
    def __init__(self, name, dept, sal):
        self.name = name        # public
        self._department = dept # private
        self.__salary = sal     # protected
    
    def display(self):
        print("Name of employee: ",self.name)
        print("Dept of employee: ",self._department)
        print("Salary of employee: ",self.__salary)

def main():
    empObj = Employee("Rahul", "Commerce", 50000.0)
    print("Employee initial details are..")
    empObj.display()
    print("\nUpdating employee information..")
    empObj.name = "Rahul Jadhav"
    empObj._department = "Commerce department"  # Protected memebers can modify
    empObj.__salary = 51000.0                   # Private members can not modify
    empObj.display()

if __name__ == "__main__":
    main()