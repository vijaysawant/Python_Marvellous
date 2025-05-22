"""
1. WAP using a while loop to print number from 1 to 50

Output : 1 2 3 4 ..... 50
"""

def main():
    print("Printing numbers from 1 to 50")
    for i in range(50):
        print(i+1, end=" ")
    print()

if __name__ == "__main__":
    main()