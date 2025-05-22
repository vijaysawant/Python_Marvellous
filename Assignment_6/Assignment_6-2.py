"""
2. Print sum of even numbers between 1 to 100. Use a loop to find and print the sum of all even numbers 
from 1 to 100

Output:
Sum of even numbers between 1 to 100 is : 2550
"""

def main():
    result = 0
    for i in range(1, 101):
        if i % 2 == 0:
            result = result + i
    print("Sum of numbers between 1 to 100 is : ",result)

if __name__ == "__main__":
    main()