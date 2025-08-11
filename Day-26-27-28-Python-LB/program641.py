# Return maximum from the list
def Maximum(brr):
    iMax = brr[0]
    for i in range(1, len(brr)):
        if brr[i] > iMax:
            iMax = brr[i]
    return iMax

def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = Maximum(Arr)
    print(f"Maximum Number : {iRet}")

if __name__ == "__main__":
    main()