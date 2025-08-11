# Accept list and return sub array/list with even numbers
def ReturnEven(Brr):
    i = 0
    Crr = []
    for i in range(len(Brr)):
        if Brr[i] % 2 == 0:
            Crr.append(Brr[i])
    return Crr
def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = ReturnEven(Arr)
    print(f"Reverse array {iRet}")

if __name__ == "__main__":
    main()