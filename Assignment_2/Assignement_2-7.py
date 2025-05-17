"""
7. WAP which accept one number and display below pattern.
Input: 5
Output:
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5
1   2   3   4   5

"""

def main():
    num = int(input("Enter number : "))
    for iRow in range(num):
        for i in range(0, num):
            print(f"{i+1}    ", end="")
        print("\n")

if __name__ == "__main__":
    main()