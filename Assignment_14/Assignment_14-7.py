"""
7. Create a base class Person with name and age. Derive a class Teacher with subject and salary. 
Use super() to call base class constructor and print both.
"""


class Person:
    def __init__(self, name, age):
        print("-- Inside Parent class constructor --")
        self.name = name
        self.age = age
    
    def displayInformation(self):
        print("Name of Person: ",self.name)
        print("Age of person: ",self.age)

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        print("-- Inside Child class constructor --")
        self.subject = subject
        self.salary = salary
    
    def displayInformation(self):
        super().displayInformation()
        print("Subject Name: ", self.subject)
        print("Salary details: ",self.salary)

def main():
    obj = Teacher(name="Sanjay", age=30, subject="English", salary=25000.0)
    obj.displayInformation()

if __name__ == "__main__":
    main()