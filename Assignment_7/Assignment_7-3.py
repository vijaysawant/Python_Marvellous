"""
Accept a list of numbers and use filter() to keep only even numbers.
Input:
Enter list: 1 2 3 4 5 6

Output:
Even numbers: [2, 4, 6]
"""

evenElements = lambda num: num%2 == 0

def main():
    print("Enter list of 6 elements : ")
    inputList = list()
    for _ in range(6):
        inputList.append(int(input("< ")))
        print("Elements in list : ",inputList)
    
    outputList = list(filter(evenElements,inputList))
    print("Print even numbers : ",outputList)

if __name__ == "__main__":
    main()