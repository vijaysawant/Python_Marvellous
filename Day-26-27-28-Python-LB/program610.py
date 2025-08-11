# Check number is divisible by 3 and 5
def CheckDivisible(No):
    if No % 3 == 0 and No % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter number : ")
    value = int(input())

    bRet = CheckDivisible(value)
    if bRet:
        print(f"Number {value} is divisible by 3 & 5")
    else:
        print(f"Number {value} is not divisible by 3 &(or) 5")

    
if __name__ == "__main__":
    main()