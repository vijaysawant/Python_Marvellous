# Check concept call by reference or call by value
# Proven: python uses call by reference
 
def Update(Brr):
    i = 0
    
    for i in range(len(Brr)-1,-1,-1):
        if Brr[i] % 2 == 0:
            Brr[i] = Brr[i] + 1
    return Brr
def main():
    iLength = int(input("Enter the number of elements : "))

    Arr = []
    print("Please enter the elements :")

    for i in range(1, iLength+1):
        no = int(input())
        Arr.append(no)

    iRet = Update(Arr)
    print(f" {iRet}")

if __name__ == "__main__":
    main()