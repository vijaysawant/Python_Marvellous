"""
6 . Write a program which accept number from user and check whether that number is positive or negative or zero
Input : 11      Output : Positive Number
Input : -8      Output : Negative Number
Input : 0      Output : Zero
"""

def main():
    Num = int(input("Enter number : "))
    if Num < 0:
        print(f"{Num} is Negative Number")
    elif Num > 0:
        print(f"{Num} is Positive Number")
    else:
        print(f"Number is Zero")

if __name__ == "__main__":
    main()