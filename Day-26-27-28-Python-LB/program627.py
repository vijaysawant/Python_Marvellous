# Reverse the number
def ReverseDigits(iNo):
    iDigit = 0
    iReverse = 0
    while iNo != 0:
        iDigit = iNo % 10
        iReverse = (iReverse * 10) + iDigit
        iNo = iNo // 10
    return iReverse


def main():
    iValue = int(input("Enter number : "))
    iRet = ReverseDigits(iValue)
    print(f"Reverse number of {iValue} is : {iRet}")

if __name__ == "__main__":
    main()