"""
8. Write a program which accept number from user and print that number of "*" on screen.
Input : 5    Output :   *   *   *   *   *
"""

def main():
    Num = int(input("Enter number : "))
    for _ in range(Num):
        print("*", end="    ")
    print("\n")

if __name__ == "__main__":
    main()