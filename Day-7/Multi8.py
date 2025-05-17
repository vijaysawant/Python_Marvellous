# Demonstration of serial execution

import threading
import time

def SumEven(no):
    sum = 0
    for i in range(2, no+1, 2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    sum = 0
    for i in range(1, no+1, 2):
        sum = sum + i
    print(sum)


def main():
    print("Demonstration of serial execution")

    start_time = time.time()    # return time in seconds
    ret1 = SumEven(90000000)
    ret2 = SumOdd(90000000)
    end_time = time.time()

    print("Time required for execution : ", end_time-start_time)
    print("End of main")

if __name__ == "__main__":
    main()