# FMR - filter map reduce concept in python
# All functions are regular functions (no use of lambda function)

from functools import reduce

def CheckEven(No):
    return (No%2 == 0)

def Increase(No):
    return No + 1

def Sum(A,B):
    return A+B

Data = [7, 10, 15, 12, 4, 6 , 9, 8 ,12, 16]
print("Input data : ",Data)

FData = list(filter(CheckEven, Data))
print("Filter output : ",FData)

MData = list(map(Increase, FData))
print("Map output : ",MData)

RData = reduce(Sum, MData)
print("Reduce output : ",RData)