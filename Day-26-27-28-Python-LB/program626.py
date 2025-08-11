# count even digits from the number
def CountEvenDigits(iNo):
    iCount = 0
    iDigit = 0
    while (iNo != 0):
        iDigit = iNo % 10
        if iDigit % 2 == 0:
            iCount = iCount + 1
        iNo = iNo // 10
    return iCount

def main():
    iValue = int(input("Enter number : "))
    iRet = CountEvenDigits(iValue)
    print(f"Number of event digits in {iValue} are : {iRet}")

if __name__ == "__main__":
    main()