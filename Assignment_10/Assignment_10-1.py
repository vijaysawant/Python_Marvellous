"""
1. Write a program which contains one lambda function which accepts one parameter and return power of two.
Input: 4    Output: 16
Input: 6    Output: 36
"""

PowerOfTwo = lambda num: num**2

inputNum = int(input("Enter number : "))
print(f"Power of {inputNum} : ",PowerOfTwo(inputNum))