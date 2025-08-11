# Reverse the array elements
def ReverseArray(Brr):
    i = 0
    Crr = []
    for i in range(len(Brr)-1,-1,-1):
        Crr.append(Brr[i])
    return Crr
def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = ReverseArray(Arr)
    print(f"Reverse array {iRet}")

if __name__ == "__main__":
    main()