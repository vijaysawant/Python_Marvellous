"""
2. WAP which accept N numbers from user and store it into List. Return Maximum number from that List.

Input: Number of elements : 7
Input Elements : 13   5   45   7   4   56   34   6
Output : 56

"""
def MaxElementFromList(myList):
    iMax = 0
    listLength = len(myList)
    for i in myList:
        if i > iMax:
            iMax = i
    return iMax

def main():
    totalNum = int(input("Enter number you want to accept : "))
    inputList = list()
    inputNum = 0
    retVal = 0
    for i in range(totalNum):
        inputNum = int(input(f"Enter number {i+1} : "))
        inputList.append(inputNum)
    print("Entered elements : ",inputList)
    retVal = MaxElementFromList(inputList)
    print("Maximum number from all elements in list : ", retVal)


if __name__ == "__main__":
    main()