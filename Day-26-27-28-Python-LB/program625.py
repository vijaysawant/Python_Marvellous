# Input 721 
# output :
# 10

def DisplayDigits(No):
    iDigit = 0
    iSum = 0
    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
    return iSum

def main():
    print("Enter number : ")
    Value = int(input())
    iRet = DisplayDigits(Value)
    print(f"Sum of digits {Value} is {iRet}")
    
if __name__ == "__main__":
    main()