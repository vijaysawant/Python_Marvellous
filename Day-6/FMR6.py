# Creating our own version of filter - map - reduce

CheckEven = lambda No : No%2 == 0
Increase = lambda No : No + 1
Sum =  lambda A,B : A + B


def filter_X(Task, Values):
    FResult = []
    for no in Values:
        if Task(no) == True:
            FResult.append(no)
    return FResult

def map_X(Task, Values):
    Result = []
    for no in Values:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def reduce_X(Task, Values):
    Result = 0
    for no in Values:
        Result = Task(Result, no)

    return Result


def main():
    Data = [7, 10, 15, 12, 4, 6 , 9, 8 ,12, 16]
    print("Input data : ",Data)

    FData = list(filter_X(CheckEven, Data))
    print("Filter output : ",FData)

    MData = list(map_X(Increase, FData))
    print("Map output : ",MData)

    RData = reduce_X(Sum, MData)
    print("Reduce output : ",RData)

if __name__ == "__main__":
    main()