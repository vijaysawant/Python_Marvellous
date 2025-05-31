"""
4. Create a Python program that Compare execution time of summing numbers from 1 to 10 million using normal
function, threading and multiprocessing.
"""

import multiprocessing.process
import time
import os
import threading
import multiprocessing


def SumNumbers(inputList):
    # sum() built-in function 
    # It returns addition of all elements of iteratable object
    print("  Sum of 1 to 10 : ",sum(inputList))

def main():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    
    # Regular function
    s_time = time.time()
    print("-- Use of regular function --")
    SumNumbers(inputList)
    e_time = time.time()
    time_taken = e_time - s_time
    print("  Time taken in seconds : ",time_taken,end="\n")

    # Using multi-threading
    s_time = time.time()
    print("-- Use of multi threading --")
    Thread = threading.Thread(target=SumNumbers, args=(inputList,))
    Thread.start()
    Thread.join()
    e_time = time.time()
    time_taken = e_time - s_time
    print("  Time taken in seconds : ",time_taken,end="\n")

    # Using multi-processing
    s_time = time.time()
    print("-- Use of multi processing --")
    process = multiprocessing.Process(target=SumNumbers, args=(inputList,))
    process.start()
    process.join()
    e_time = time.time()
    time_taken = e_time - s_time
    print("  Time taken in seconds : ",time_taken,end="\n")
if __name__ == "__main__":
    main()