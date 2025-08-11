# Add elements of the list
def Addition(brr):
    iSum = 0
    for no in brr:
        iSum += no
    return iSum

def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = Addition(Arr)
    print(f"Addition of all elements : {iRet}")

if __name__ == "__main__":
    main()