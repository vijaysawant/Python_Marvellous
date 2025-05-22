"""
3. Accept a number from the user and print its multilpcation table up to 10.

Input: 
Enter a number : 7
Output:
7 x 1 = 7
7 x 2 = 14
. . .
7 x 10 = 70
"""

def main():
    inputNum = int(input("Enter a number : "))
    for i in range (1, 11):
        print(f"{inputNum} x {i} = {inputNum*i}")

if __name__ == "__main__":
    main()