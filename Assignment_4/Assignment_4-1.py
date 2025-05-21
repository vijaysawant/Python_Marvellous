"""
1. WAP which contains one lambda function which accepts one parameter and return power of two.
Input: 4    Output: 16
Input: 8    Output: 64
"""

PowerOfTwo = lambda num: num * num

inputNum = int(input("Enter number : "))
print(f"Power of {inputNum} : ",PowerOfTwo(inputNum))