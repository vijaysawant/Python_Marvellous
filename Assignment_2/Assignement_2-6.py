"""
6. WAP which accept one number and dispaly below pattern.
Input: 5
Output:
*   *   *   *   *
*   *   *   *
*   *   *
*   *
*

"""


def main():
    num = int(input("Enter number : "))
    for iRow in range(num):
        for _ in range(iRow, num):
            print("*    ", end="")
        print("\n")

if __name__ == "__main__":
    main()