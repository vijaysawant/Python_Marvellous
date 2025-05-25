# Basics of OOP - Types of Characteristics and types of Behaviours
"""
Class variable and Instance variable
CompanyName is Class variable and Name, Salary, City are Instance varibles
"""
class Employee:
    CompanyName = "Marvellous"

    def __init__(self,A,B,C):
        print("--Inside Constructor--")
        self.Name = A
        self.Salary = B
        self.City = C

    def __del__(self):
        print("--Inside Destructor--")

def main():
    print("Class variable : "+Employee.CompanyName)

    emp1 = Employee('Rahul',15000,'Pune')
    emp2 = Employee('Pooja',25000,'Mumbai')

    print("Employee Name : "+emp1.Name)
    print("Employee Salary : ",emp1.Salary)
    print("Employee City : "+emp1.City)

if __name__ == "__main__":
    main()