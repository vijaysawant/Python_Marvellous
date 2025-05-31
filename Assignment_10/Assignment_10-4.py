"""
4. WAP which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which are even.
Map function will calculate its square.
Reduce will return addition of all that numbers.

Input List = [5,2,3,4,3,4,1,2,8,10]
List after filter = [2,3,3,2,8,10]
List after map = [4,16,16,4,64,100]
Output of reduce = 204
"""
from functools import reduce

boolEven = lambda num : num%2 == 0    # Return true if number is even false otherwise
CalSquare = lambda num : num*num        # Return square of number
SumNumbers = lambda num1,num2 : num1+num2   # Return addition of numbers


def main():
    # inputList = [5,2,3,4,3,4,1,2,8,10]
    inputList = list()
    totalNum = int(input("Enter how many numbers : "))
    for i in range(totalNum):
        inputList.append(int(input(f"Enter {i + 1} number : ")))
    print("You entered list : ",inputList)
    F_dataList = list(filter(boolEven, inputList))
    print("Filter Output : ",F_dataList)

    M_dataList = list(map(CalSquare, F_dataList))
    print("Map Output : ", M_dataList)
    
    R_data = reduce(SumNumbers, M_dataList)
    print("Reduce Output : ", R_data)

if __name__ == "__main__":
    main()