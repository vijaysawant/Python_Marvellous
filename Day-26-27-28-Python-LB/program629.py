# Calculate occurance of multiple digits
def CountOccuranceOfX(iNo):
    iCount4 = 0
    iCount5 = 0
    iCount7 = 0
    iDigit = 0
    while(iNo != 0):
        iDigit = iNo % 10
        if iDigit == 4:
            iCount4 += 1
        elif iDigit == 5:
            iCount5 += 1
        elif iDigit == 7:
            iCount7 += 1
        iNo = iNo // 10
    return iCount4, iCount5, iCount7

def main():
    iValue = int(input("Enter number : "))

    iRet4,iRet5,iRet7 = CountOccuranceOfX(iValue)
    print(f"Occurances of 4 => {iRet4}, 5 => {iRet5} and 7 => {iRet7}")

if __name__ == "__main__":
    main()