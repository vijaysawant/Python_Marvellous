# Creating our own version of filter - map - reduce
# Accpeting input from user at run time

import MarvellousFMR

CheckEven = lambda No : No%2 == 0
Increase = lambda No : No + 1
Sum =  lambda A,B : A + B


def main():
    Data = []
    NumOFElements = int(input("Enter number of elements : "))
    print("Please enter numeric values : ")
    for i in range(NumOFElements):
        no = int(input())
        Data.append(no)

    print("Input data : ",Data)

    FData = list(MarvellousFMR.filter_X(CheckEven, Data))
    print("Filter output : ",FData)

    MData = list(MarvellousFMR.map_X(Increase, FData))
    print("Map output : ",MData)

    RData = MarvellousFMR.reduce_X(Sum, MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()