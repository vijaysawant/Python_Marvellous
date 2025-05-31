"""
2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input: 4    3    Output: 12
Input: 6    3    Output: 18
"""
MultiplyNumbers = lambda num1,num2:num1 * num2


Num1 = int(input("Enter num 1 : "))
Num2 = int(input("Enter num 2 : "))
print(f"Multiplication of {Num1} & {Num2} :",MultiplyNumbers(Num1,Num2))