# Multi-core programming

import os
import time
import multiprocessing

# addition of cube of number
def fun(no):
    print("PID is : ",os.getpid())  # PID will different
    sum = 0
    for i in range(1, no):
        sum = sum + (i*i*i)
    return sum

def main():
    s_time = time.time()
    
    data = [100000, 200000, 300000, 400000, 500000, 6000000,7000000,8000000,9000000,10000000]
    result = []
    
    p = multiprocessing.Pool()
    result = p.map(fun, data)

    p.close()
    p.join()

    print(result)

    e_time = time.time()
    print(">> Time required : ",e_time-s_time)

if __name__ == "__main__":
    main()