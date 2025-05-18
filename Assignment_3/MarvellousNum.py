def ListPrime(inputList):
    # This function return addition of all prime numbers from list
    SumOfPrime = 0
    if len(inputList) == 0:
        return None
    for Num in inputList:
        if __CheckPrime(Num) == True:
            # print("Prime : ",Num)
            SumOfPrime = SumOfPrime + Num
    return SumOfPrime


def __CheckPrime(Num):
    IsPrime = True
    for i in range(2, Num):
        if Num % i  == 0:
            IsPrime = False
    return IsPrime