"""
1. Create one module named as Arithmatic which contains 4 functions as Add() for addition, Sub() for substraction, Mult() 
and Div() respectively. All functions accepts two parameters as number and perform the operations. Write one python program which
call all the functions from Arithmatic module by accepting the parameters from user.
"""

import ArithmaticOperations as Arithmantic

def main():
    print("Accept user input for Arithmatic operations")
    # print("\nAccept user input for Addition")
    Num1 = int(input("Enter 1st number : "))
    Num2 = int(input("Enter 2nt number : "))
    Arithmantic.Add(Num1, Num2)

    # print("\nAccept user input for Substraction")
    # Num1 = int(input("Enter 1st number : "))
    # Num2 = int(input("Enter 2nt number : "))
    Arithmantic.Sub(Num1, Num2)

    # print("\nAccept user input for Multiplication")
    # Num1 = int(input("Enter 1st number : "))
    # Num2 = int(input("Enter 2nt number : "))
    Arithmantic.Mult(Num1, Num2)

    # print("\nAccept user input for Division")
    # Num1 = int(input("Enter 1st number : "))
    # Num2 = int(input("Enter 2nt number : "))
    Arithmantic.Div(Num1, Num2)


if __name__ == "__main__":
    main()