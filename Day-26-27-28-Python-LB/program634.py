# Check number is perfect or not, time complexity is N/2

def CheckPerfect(iNo):
    iSum = 0
    for i in range(1, (iNo//2)+1):
        if iNo % i == 0:
            iSum += i
    return (iSum == iNo)

def main():
    iValue = int(input("Enter number : "))
    bRet = CheckPerfect(iValue)
    if bRet:
        print(f"Number {iValue} is perfect")
    else:
        print(f"Number {iValue} is not perfect")


if __name__ == "__main__":
    main()