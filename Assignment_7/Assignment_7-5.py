"""
Write a function that accepts a string and check whether it is a palindrome.
Input:
Enter a string: radar

Output:
radar is palindrome
"""

def ChkPalindrome(inputStr):
    reverse_Str = ""
    inputStrLen = len(inputStr)
    for index in range(inputStrLen-1, -1 ,-1):
        reverse_Str = reverse_Str + inputStr[index]
    print("Generated reverse string : ",reverse_Str)

    if inputStr != reverse_Str:
        print(f"{inputStr} and {reverse_Str} doesn't match")
        return False
    
    return True

def main():
    inputStr = input("Enter string : ")
    outResult = ChkPalindrome(inputStr)
    if outResult:
        print(f"{inputStr} is palindrom")
    else:
        print(f"{inputStr} is not palindrom")
if __name__ == "__main__":
    main()