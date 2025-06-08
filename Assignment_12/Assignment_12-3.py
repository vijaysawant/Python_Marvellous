"""
3. WAP which contains one class named as Arithmetic,
Arithmetic class contains three instance variables as Value1, Value2.
Inside init method initialse all instance varibales to 0.
THere are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1, VAlue2 and return result.
Substraction() method will perform substraction of Value1, VAlue2 and return result.
Multiplication() method will perform multiplication of Value1, VAlue2 and return result.
Division() method will perform division of Value1, VAlue2 and return result.
After desining the above class call all instance methods by creating multiple objects.
"""

class Arithmetic:
    def __init__(self):
        self.Result = 0
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self, val1, val2):
        self.Value1 = val1
        self.Value2 = val2

    def Addition(self):
        self.Result = self.Value1 + self.Value2
        return self.Result

    def Substraction(self):
        self.Result = self.Value1 - self.Value2
        return self.Result
        
    def Multiplication(self):
        self.Result = self.Value1 * self.Value2
        return self.Result

    def Division(self):
        try:
            self.Result = self.Value1 / self.Value2
        except ZeroDivisionError as zde:
            print("Error while perfoming operation : ", zde)
            self.Result = None
        return self.Result


def main():
    obj = Arithmetic()
    obj.Accept(20,10)
    print("Addition is: ",obj.Addition())
    print("Subsctraction is: ",obj.Substraction())
    print("Multiplication is: ",obj.Multiplication())
    print("Division is: ",obj.Division())

    print()
    obj2 = Arithmetic()
    obj2.Accept(20,0)
    print("Addition is: ",obj2.Addition())
    print("Subsctraction is: ",obj2.Substraction())
    print("Multiplication is: ",obj2.Multiplication())
    print("Division is: ",obj2.Division())

if __name__ == "__main__":
    main()