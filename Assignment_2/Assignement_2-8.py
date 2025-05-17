"""
8. WAP which accept one number and display below pattern.
Input: 5
Output:
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5

"""

def main():
    num = int(input("Enter number : "))
    for iRow in range(num):
        for iCol in range(num):
            if iRow >= iCol:
                print(iCol+1, end=" ")
            else:
                continue
        print("\n")

if __name__ == "__main__":
    main()