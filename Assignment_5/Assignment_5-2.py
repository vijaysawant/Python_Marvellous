"""
2. Vowel or Consonant check
Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print it's a consonant.

Input: 
Enter a character: e

Output:
'e' is a vowel.
"""


def main():
    singleChar = input("Enter single character : ")
    if singleChar in ('a','e','i','o','u'):
        print(f"{singleChar} is a vowel")
    elif singleChar in ('A','E','I','O','U'):
        print(f"{singleChar} is a vowel")
    else:
        print(f"{singleChar} is a consonant")

if __name__ == "__main__":
    main()