"""
Input: HELLO
Output: 
H   E   L   L   O
H   E   L   L   O
H   E   L   L   O
H   E   L   L   O
H   E   L   L   O
"""


def Display(input):
    for _ in range(len(input)):
        for ch in input:
            print(ch, end="\t")    
        print()
    print()
    
def main():
    print("Enter the string : ")
    str = input()
    Display(str)

if __name__ == "__main__":
    main()