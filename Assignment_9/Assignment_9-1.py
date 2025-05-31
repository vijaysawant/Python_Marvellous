"""
1. Create a Python program that starts 3 threads, each printing numbers from 1 to 5 with a delay
of 1 second. 
Use threading.Thread
"""
import threading
import time

def one():
    print("First Thread")
    for i in range(5):
        print(i+1)
        time.sleep(1)

def two():
    print("Second Thread")
    for i in range(5):
        print(i+1)
        time.sleep(1)

def three():
    print("Third Thread")
    for i in range(5):
        print(i+1)
        time.sleep(1)

def main():
    T1 = threading.Thread(target=one)
    T2 = threading.Thread(target=two)
    T3 = threading.Thread(target=three)

    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()

if __name__ == "__main__":
    main()