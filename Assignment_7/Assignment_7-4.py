"""
4. Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.

Input:
Enter list: 2 3 4
Output:
Product: 24
"""
from functools import reduce

returnProduct = lambda num1, num2: num1*num2

def main():
    print("Enter list of 3 elements : ")
    inputList = list()
    for _ in range(3):
        inputList.append(int(input("< ")))
        print("Elements in list : ",inputList)
    
    outputList = reduce(returnProduct,inputList)
    print("Print product of all elements : ",outputList)

if __name__ == "__main__":
    main()