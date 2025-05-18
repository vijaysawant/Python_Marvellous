"""
1. WAP which accept N numbers from user and store it into List. Return addition of all elements from that list

Input: Number of elements : 6
Input Elements : 13   5   45   7   4   56
Output : 130
"""

def ReturnAdditionOfElements(myList):
    sum = 0
    cnt = len(myList)
    for i in range(cnt):
        sum = sum + myList[i]
    return sum

def main():
    totalNum = int(input("Enter number you want to accept : "))
    inputList = list()
    inputNum = 0
    retVal = 0
    for i in range(totalNum):
        inputNum = int(input(f"Enter number {i+1} : "))
        inputList.append(inputNum)
    print("Entered elements : ",inputList)
    retVal = ReturnAdditionOfElements(inputList)
    print("Addition of all elements in list : ", retVal)


if __name__ == "__main__":
    main()