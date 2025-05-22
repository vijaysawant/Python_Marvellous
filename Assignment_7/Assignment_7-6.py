"""
Write a function that accepts a list of integers and return a list of prime numbers using filter().
Input:
Enter list: 10 11 12 13 14 15 16 17

Output:
Prime numbers: [11, 13, 17]
"""

def IsPrime(input):
    Prime = True
    for i in range(2, input):
        if input % i == 0:
            Prime = False
            break
    return Prime

def main():
    print("Enter elements using spaces : ", end="")
    inputDetails = input()
    print("Entered input type is : ",type(inputDetails))

    print(f"\nConvert {type(inputDetails)} object into expected format")
    # Split function will split string using seperator as " " (spaces) and convert into 'list of strings'
    InputDetails = inputDetails.split(" ")
    # Now convert each element of list from string to integ, use list comprehension
    InputDetails = [int(strElement) for strElement in InputDetails]
    print(f"Converted list of integers of type {type(InputDetails)} : ", InputDetails)

    F_Data = list(filter(IsPrime, InputDetails))
    print("\nPrime numbers : ",F_Data)

if __name__ == "__main__":
    main()
