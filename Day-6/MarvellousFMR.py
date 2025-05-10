# Creating our own version of filter - map - reduce

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