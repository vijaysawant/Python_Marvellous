"""
6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user input for values 
and call methods accordingly.
"""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

def main():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    obj = Calculator(num1, num2)
    print("Addition is: ",obj.add())
    print("Substraction is : ",obj.subtract())
    print("Multiplication is: ",obj.multiply())
    print("Division is: ",obj.divide())
    print()
    
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    obj1 = Calculator(num1, num2)
    print("Addition is : ",obj1.add())
    print("Substraction is : ",obj1.subtract())
    print("Multiplication is ",obj1.multiply())
    print("Division is ",obj1.divide())

if __name__ == "__main__":
    main()