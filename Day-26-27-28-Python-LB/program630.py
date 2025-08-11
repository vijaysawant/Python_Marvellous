# Factors of number

def DisplayFactors(iNo):
    print(f"Factors of {iNo} are : ",end="")
    for i in range(1, iNo):
        if iNo % i == 0:
            print(i, end=" ")
    print()

def main():
    iValue = int(input("Enter number : "))
    DisplayFactors(iValue)


if __name__ == "__main__":
    main()