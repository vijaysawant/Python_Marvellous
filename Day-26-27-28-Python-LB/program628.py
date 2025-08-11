# Calculate occurance of 5 in the digit
def CountOccuranceOfX(iNo):
    iCount = 0
    iDigit = 0
    while(iNo != 0):
        iDigit = iNo % 10
        if iDigit == 5:
            iCount += 1
        iNo = iNo // 10
    return iCount

def main():
    iValue = int(input("Enter number : "))

    iRet = CountOccuranceOfX(iValue)
    print(f"Occurance of 5 ibn {iValue} is : {iRet}")

if __name__ == "__main__":
    main()