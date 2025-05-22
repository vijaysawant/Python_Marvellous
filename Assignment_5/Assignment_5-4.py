"""
4. Find largest among three numbers
Accept three numbers from the user and print the largest using nested if-else statements.

Input:
Enter three numbers: 5 9 3
Largest number is 9
"""

def main():
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    num3 = int(input("Enter 3rd number : "))

    largest = 0
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num3 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    
    print("Largetst number is ",largest)


if __name__ == "__main__":
    main()