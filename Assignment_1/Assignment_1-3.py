"""
3 . Write a program which contains one function named as Add() which accepts two numbers from user
 and return addition of that two numbers.
Input : 11 5    Output : 16
"""

def Add(Num1, Num2):
    OutVal = 0
    OutVal = Num1 + Num2
    return OutVal

def main():
    Num1 = int(input("Enter number 1 : "))
    Num2 = int(input("Enter number 2 : "))
    Result = Add(Num1, Num2)
    print(f"Addtion of {Num1} and {Num2} is {Result}")

if __name__ == "__main__":
    main()