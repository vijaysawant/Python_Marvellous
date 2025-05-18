"""
5. WAP which accept N numbers from user and store it into List. Return addition of all prime numbers from that
List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of
our defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

Inpuut : Number of Element : 11
Input Elements : 13   5   45    7   4   56  10  34  2   5   8
Output : 32 (13 + 5 + 7 + 2 + 5)
"""
import MarvellousNum

def main():
    totalNum = int(input("Enter number you want to accept : "))
    inputList = list()
    inputNum = 0
    retVal = 0
    for i in range(totalNum):
        inputNum = int(input(f"Enter number {i+1} : "))
        inputList.append(inputNum)

    print("\nEntered elements : ",inputList)
    retVal = MarvellousNum.ListPrime(inputList)
    print("\nAddition of Prime numbbers from the list : ",retVal)


if __name__ == "__main__":
    main()