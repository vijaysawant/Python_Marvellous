"""
7. Accept 5 numbers from the user. Find and print the largest number.
Input:
Enter 5 numbers: 23 89 12 56 45

Output:
Maximum number is: 89
"""

### TODO:Is this possible to use functtools.reduce method here, if yes try to use ###
# import functools

# def FindMaxNum_Reduce(num):
#     max = 0
#     if num > max:
#         max = num
#     return max

def FindMaxNum(inputList):
    max = 0
    for num in inputList:
        if num > max:
            max = num
    return max

def main():
    totalNum = int(input("Enter total numbers : "))
    numList = list()
    for _ in range(totalNum):
        num = int(input("Enter number : "))
        numList.append(num)
    maxNum = FindMaxNum(numList)
    print("Maximum number is : ",maxNum)

    # numList = [23, 89, 12, 56, 45]
    # print("Input list : ", numList)
    # print("Maximum number : ", functools.reduce(FindMaxNum_Reduce, numList))
if __name__ == "__main__":
    main()