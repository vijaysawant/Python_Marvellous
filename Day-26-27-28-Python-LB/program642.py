# Return minimum from the list
def Minimum(brr):
    iMin = brr[0]
    for i in range(1, len(brr)):
        if brr[i] < iMin:
            iMin = brr[i]
    return iMin

def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = Minimum(Arr)
    print(f"Minimun Number : {iRet}")

if __name__ == "__main__":
    main()