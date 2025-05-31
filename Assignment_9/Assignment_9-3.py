"""
3. Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.
"""
import multiprocessing.pool
import time
import multiprocessing
import os

def computeFactorial(inputNum):
    print(f"Process computeFactorial ID : {os.getppid()}")
    factorial = 1
    for i in range(1, inputNum+1):
        factorial = factorial * i
    print(f"Factorial of {inputNum} is {factorial}")

def main():
    inputList = [1,2,3,4,5,6,7,8,9,10]

    # without use of multiprocessing.Pool()
    s_time = time.time()
    for i in inputList:
        process1 = multiprocessing.Process(target=computeFactorial, args=(i,))
        process1.start()
        process1.join()
    e_time = time.time()
    print("Time require in second : ",e_time-s_time)
    print()

    # with use of multiprocessing.Pool()
    s_time = time.time()
    mutliprocessPool = multiprocessing.Pool()
    res = mutliprocessPool.map(computeFactorial, inputList)
    mutliprocessPool.close()
    mutliprocessPool.join()

    e_time = time.time()
    print("Time require in second : ",e_time-s_time)

if __name__ == "__main__":
    main()