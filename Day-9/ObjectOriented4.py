"""
Class variable and Instance variable
CompanyName is Class variable and Name, Salary, City are Instance varibles
"""
class Employee:
    CompanyName = "Marvellous"          # Class variable

    def __init__(self,A,B,C):           # -- Constructor -- #
        print("--Inside Constructor--")
        self.Name = A                   # Instance variable
        self.Salary = B                 # Instance variable
        self.City = C                   # Instance variable

    def __del__(self):                  # -- Destructor -- #
        print("--Inside Destructor--")

    def DisplayInfo(self):              # Instance method
        print("\n--Inside Instance method : DisplayInfo--")
        print("Employee Name : "+self.Name)
        print("Employee Salary : ",self.Salary)
        print("Employee City : "+self.City)
    
    @classmethod
    def DisplayCompanyDetails(cls):     # Class method
        print("\n--Inside Class method : DisplayCompanyDetails--")
        print("Company Name : "+cls.CompanyName)
    
    @staticmethod
    def DisplayCompanyPolicy():         # Static method
        print("\n--Inside Static method : DisplayCompanyPOlicy--")
        print("All employees are 18+")
        print("Working hours are 9 to 6")
        print("Holidays : Saturday & Sunday")

def main():
    print("Class variable : "+Employee.CompanyName)
    Employee.DisplayCompanyDetails()

    emp1 = Employee('Rahul',15000,'Pune')       # Object creation
    emp2 = Employee('Pooja',25000,'Mumbai')     # Object creation

    print("Employee Name : "+emp1.Name)
    print("Employee Salary : ",emp1.Salary)
    print("Employee City : "+emp1.City)

    emp2.DisplayInfo()
    Employee.DisplayCompanyPolicy()

    del emp1
    del emp2

if __name__ == "__main__":
    main()