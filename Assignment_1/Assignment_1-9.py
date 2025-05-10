"""
9. Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
"""

def main():
    TotalNumber = 10
    Number = 1
    print("Using while loop")
    print(f"First {TotalNumber} even numbers : ", end="")
    while Number <= TotalNumber:
        print(Number*2, end=" ")
        Number = Number + 1
    print("")

    print("Using for loop")
    print(f"First {TotalNumber} even numbers : ", end="")
    for cnt in range(1, 11):
        print(cnt*2, end=" ")
    print("")
if __name__ == "__main__":
    main()