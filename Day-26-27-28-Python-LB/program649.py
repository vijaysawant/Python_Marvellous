# Reverse the list inplace
 
def ReverseList_Inplace(Brr):
    iStart = 0
    iEnd = len(Brr)-1
    iElement = 0
    while(iStart < iEnd):
        iElement = Brr[iStart]
        Brr[iStart] = Brr[iEnd]
        Brr[iEnd] = iElement
        iStart += 1
        iEnd -= 1
    return Brr


def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = ReverseList_Inplace(Arr)
    print(f"Inplace reverse list {iRet}")

if __name__ == "__main__":
    main()