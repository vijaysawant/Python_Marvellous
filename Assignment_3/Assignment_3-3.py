"""
3. WAP which accept N numners from user and store it into List. Return Minimum number from that List.

Input: Number of elements : 4
Input Elements : 13   5   45   7
Output : 5

"""

def MinElementFromList(myList):
    listLength = len(myList)
    if listLength == 0:
        print("Warning.. List were empty..")
        return None
    iMin = myList[0]
    
    for i in myList:
        if i < iMin:
            iMin = i
    return iMin


def main():
    totalNum = int(input("Enter number you want to accept : "))
    inputList = list()
    inputNum = 0
    retVal = 0
    for i in range(totalNum):
        inputNum = int(input(f"Enter number {i+1} : "))
        inputList.append(inputNum)
    print("Entered elements : ",inputList)
    retVal = MinElementFromList(inputList)
    print("Minimum number from all elements in list : ", retVal)


if __name__ == "__main__":
    main()