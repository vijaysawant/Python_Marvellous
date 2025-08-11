def CheckEvenOdd(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter number : ")
    value = int(input())

    bRet = CheckEvenOdd(value)
    if bRet:
        print(f"Number {value} is Even number")
    else:
        print(f"Number {value} is Odd number")

    
if __name__ == "__main__":
    main()