# Replace charactor 'a' with underscroll (_) , inplace replacement

def ReplaceChar(input):
    for i in range(len(input)-1):
        if input[i] == 'a':
            input[i] = '_'      # Error - TypeError: 'str' object does not support item assignment

def main():
    print("Enter string : ")
    str = input()

    ReplaceChar(str)
    print(f"Replace string is {str}")

if __name__ == "__main__":
    main()