# Sum of Factors of number, time complexity is N/2

def SumFactors(iNo):
    iSum = 0
    print(f"Factors of {iNo} are : ",end="")
    for i in range(1, (iNo//2)+1):
        if iNo % i == 0:
            iSum += i
    return iSum

def main():
    iValue = int(input("Enter number : "))
    iRet = SumFactors(iValue)
    print(f"Sum of factors of {iValue} is {iRet}")


if __name__ == "__main__":
    main()