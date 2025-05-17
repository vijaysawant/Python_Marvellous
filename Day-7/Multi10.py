# Multi processing
# Demonstration of parellel execution

import multiprocessing
import time
import os

def SumEven(no):
    print("> PID of SumEven process is ",os.getpid())
    print(">> PPID of SumEven process is ",os.getppid())       # it will return 101
    sum = 0
    for i in range(2, no+1, 2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    print("> PID of SumOdd process is ",os.getpid())
    print(">> PPID of SumOdd process is ",os.getppid())       # it will return 101
    sum = 0
    for i in range(1, no+1, 2):
        sum = sum + i
    print(sum)


def main():

    print("--- Demonstration of parellel execution ---")
    print("> PID of main process : ",os.getpid())     # Suppose main PID is 101
    start_time = time.time()
    
    P1 = multiprocessing.Process(target=SumEven, args=(90000000,))
    P2 = multiprocessing.Process(target=SumOdd, args=(90000000,))
    
    P1.start()
    P2.start()

    P1.join()
    P2.join()

    end_time = time.time()

    print("Time required for execution : ", end_time-start_time)
    print("End of main")
    

if __name__ == "__main__":
    main()