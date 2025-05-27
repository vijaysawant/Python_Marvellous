"""
2. Design python application which creates two threads as evenfactor and oddfactor. Both the threads
accept one parameter as integer. Evenfactor thread will display addition of even factors of given
number and oddfactor will display addition of odd factors of given number. After execution of both the
thread gets completed main thread should display message as "exit from main".
"""

import threading

def evenfactor(value):
    print("--Inside thread ==> evenfactor")
    sum = 0
    # find sum of even-factors of 20 => 2+4+10+20 = 36
    for i in range(1,value+1):
        if i % 2 == 0 and value % i == 0:
            sum = sum + i
            # print(f"i > {i} and sum > {sum}")
    print(f"Sum of even-factors of {value} : {sum}")    # 36

def oddfactor(value):
    print("--Inside thread ==> oddfactor")
    sum = 0
    # find sum of odd-factors of 20 => 1+5 = 6
    for i in range(1, value+1):
        if i % 2 == 1 and value % i == 0:
            sum = sum + i
            # print(f"i > {i} and sum > {sum}")
    print(f"Sum of odd-factors of {value} : {sum}") # 6

def main():
    T1 = threading.Thread(target=evenfactor, args=(20,))
    T2 = threading.Thread(target=oddfactor, args=(20,))

    T1.start()
    T2.start()

if __name__ == "__main__":
    main()