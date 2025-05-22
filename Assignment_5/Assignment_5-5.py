"""
5. Even or Odd number check
WAP to check whether the entered number is even or odd.

Input:
Enter a number: 17

Outout:
17 is an odd number.
"""

def main():
    inputNum = int(input("Enter number : "))
    if inputNum % 2 == 0:
        print(f"{inputNum} is an even number")
    else:
        print(f"{inputNum} is an odd number")

if __name__ == "__main__":
    main()