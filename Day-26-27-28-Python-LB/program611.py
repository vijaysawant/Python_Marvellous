# Check maximum of 3 numbers
def ReturnMaximum(No1, No2, No3):
    if No1 > No2 and No1 > No3:
        return No1
    elif No2 > No1 and No2 > No3:
        return No2
    else:
        return No3

def main():
    print("Enter 1st number : ")
    value1 = int(input())

    print("Enter 2nd number : ")
    value2 = int(input())

    print("Enter 3rd number : ")
    value3 = int(input())

    iRet = ReturnMaximum(value1, value2, value3)
    print(f"{iRet} is the maximum number")

    
if __name__ == "__main__":
    main()