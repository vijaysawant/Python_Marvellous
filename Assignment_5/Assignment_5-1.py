"""
1. Arithmetic operations on Two numbers
WAP to accept two integers from the user and display their:
- Sum
- Difference
- Product
- Division

Expected Input:
Enter first number : 10
Enter first number : 2

Sum: 12
Difference: 8
Product: 20
Division: 5.0
"""


Sum = lambda X,Y : X+Y
Difference = lambda X,Y : X-Y
Product = lambda X,Y : X*Y
Division = lambda X,Y : X/Y

def main():
    Num1 = int(input("Enter number 1 : "))
    Num2 = int(input("Enter number 2 : "))
    
    print("Sum :",Sum(Num1, Num2))
    print("Difference :",Difference(Num1, Num2))
    print("Product :",Product(Num1, Num2))
    print("Division :",Division(Num1, Num2))

if __name__ == "__main__":
    main()