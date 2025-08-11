"""
Input: HELLO
Output: 
H   E   L   L   O
"""


def Display(input):
    for ch in input:
        print(ch, end="\t")    
    print()
    
def main():
    print("Enter the string : ")
    str = input()
    Display(str)

if __name__ == "__main__":
    main()