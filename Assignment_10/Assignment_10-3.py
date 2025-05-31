"""
3. WAP which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. Filter should filter out all such numbers which
greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10.
Reduce will return product of all that numbers.

Input List = [4,34,36,76,68,24,89,23,86,90,45,70]
List after filter = [76,89,86,90,70]
List after map = [86,99,96,100,80]
Output of reduce = 6538752000
"""
from functools import reduce

def FilterOutRange(inputData):
    """ Return True if numbers is greater than or equal to 70 and less than or equal to 90, False otherwise """
    if inputData >= 70 and inputData <= 90:
        return True
    else:
        return False

def IncreaseValue(inputData):
    """ Increase each number by 10 and return it """
    return inputData + 10


def ProductOfNumbers(input1, input2):
    """ Return product of all that numbers """
    return input1 * input2

def main():
    # inputList = [4,34,36,76,68,24,89,23,86,90,45,70]
    inputList = list()
    totalNum = int(input("Enter how many numbers : "))
    for i in range(totalNum):
        inputList.append(int(input(f"Enter {i + 1} number : ")))
    print("You entered list : ",inputList)
    F_dataList = list(filter(FilterOutRange, inputList))
    print("Filter Output : ",F_dataList)

    M_dataList = list(map(IncreaseValue, F_dataList))
    print("Map Output : ", M_dataList)
    
    R_data = reduce(ProductOfNumbers, M_dataList)
    print("Reduce Output : ", R_data)

if __name__ == "__main__":
    main()