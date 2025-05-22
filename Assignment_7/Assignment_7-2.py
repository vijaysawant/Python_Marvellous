"""
2. Accept a list of integers from the user and use the map() function to double each value.

Input:
Enter list: 1 2 3 4 5

Output:
Doubled list:   [2, 4, 6, 8, 10]
"""

# Use of list comprehension to shorten lines using lambda function
DoubleElements = lambda inputList: [i*2 for i in inputList]

# Use of regular approach using simple python function
# def DoubleElements(inputList):
#     newList = list()
#     for i in inputList:
#         newList.append(i*2)
#     return newList


def main():
    print("Enter list of 5 elements : ")
    inputList = list()
    for _ in range(5):
        inputList.append(int(input("< ")))
        print("Elements in list : ",inputList)

    print("\nAfter double list elements\nFinal output list : ", DoubleElements(inputList))


if __name__ == "__main__":
    main()