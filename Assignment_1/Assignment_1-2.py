"""
2. Write a program which contains one function named as ChkNum() which accept one parameter as number.
If number is even then it should display "Even number" otherwise display "Odd number" on console.
Input : 11      Output : Odd number
Input : 8       Output : Even number
"""

def ChkNum(Num):
    if Num % 2 == 0:
        print(f"{Num} is Even Number")
    else:
        print(f"{Num} is Odd Number")
    
if __name__ == "__main__":
    ChkNum(11)
    ChkNum(8)