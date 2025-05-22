"""
3. Voting Eligibility checker
Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)

Input:
Enter age: 19

Output:
Eligible to vote.
"""


def main():
    inputAge = int(input("Enter age : "))
    if inputAge >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

if __name__ == "__main__":
    main()