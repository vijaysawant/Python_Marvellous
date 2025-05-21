"""
5. WAP which contains filter(), map() and reduce() in it. Python application which containss one list of numbers.
List contains the numbers which are accepted from user. 
Filter should filter out all prime numbers. 
Map function will mulitply each numbers by 2. 
Reduce will return Maximum numbers from that numbers. 
(You can also use normal functions instead of lambda functions).

Input List = [2,70,11,10,17,23,31,77]
List after filter = [2,11,17,23,31]
List after map = [4,22,34,46,62]
Output of reduce = 62
"""

from functools import reduce

def CheckPrime(Num):
    # Return true if number is Prime, false otherwise
    IsPrime = True
    for i in range(2, Num):
        if Num % i  == 0:
            IsPrime = False
    return IsPrime

MultBy2 = lambda num : num*2        # Multiply by 2 and return result

def ReturnMax(num1,num2):
    maxVal = 0
    if num1 > num2:
        maxVal = num1
    else:
        maxVal = num2
    return maxVal

def main():
    # inputList = [2,70,11,10,17,23,31,77]
    inputList = list()
    totalNum = int(input("Enter how many numbers : "))
    for i in range(totalNum):
        inputList.append(int(input(f"Enter {i + 1} number : ")))
    print("You entered list : ",inputList)
    F_dataList = list(filter(CheckPrime, inputList))
    print("Filter Output : ",F_dataList)

    M_dataList = list(map(MultBy2, F_dataList))
    print("Map Output : ", M_dataList)
    
    R_data = reduce(ReturnMax, M_dataList)
    print("Reduce Output : ", R_data)

if __name__ == "__main__":
    main()