# Count even and odd elements from the list
def CountEvenOdd(brr):
    iEven = 0

    for no in brr:
        if no % 2 == 0:
            iEven += 1
        
    return iEven, len(brr) - iEven 

def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = CountEvenOdd(Arr)
    print(f"Number of even numbers => {iRet[0]} and odd numbers => {iRet[1]}")

if __name__ == "__main__":
    main()