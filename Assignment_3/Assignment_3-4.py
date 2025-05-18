"""
4. WAP which accept N numbers from user and store it into List. Accept one another number from user and
return frequency of that number from List.

Input: Number of elements : 11
Input Elements : 13   5   45   7    4   56  5   34  2   5   65
Element to search : 5
Output : 3
"""

def FindOccurenceOfNumber(myList, NumToSearch):
    listLength = len(myList)
    occurences = 0
    if listLength == 0:
        print("Warning.. List were empty..")
        return None
    for i in myList:
        if i == NumToSearch:
            occurences = occurences + 1
    return occurences


def main():
    totalNum = int(input("Enter number you want to accept : "))
    inputList = list()
    inputNum = 0
    retVal = 0
    for i in range(totalNum):
        inputNum = int(input(f"Enter number {i+1} : "))
        inputList.append(inputNum)
    NumToSearch = int(input("Number to search : "))
    print("\nEntered elements : ",inputList)
    retVal = FindOccurenceOfNumber(inputList, NumToSearch)
    print(f"\nTotal occurences of {NumToSearch} in list are {retVal} times")


if __name__ == "__main__":
    main()