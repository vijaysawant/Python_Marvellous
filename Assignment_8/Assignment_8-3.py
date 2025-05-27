"""
3. Design python application which creates two threads as evenlist and oddlist. Both the threads accept
list of integers as parameter. Evenlist thread add all even elements from input list and display the
addition. Oddlist thread add all odd elements from input list and display the addition.
"""

import threading

def evenlist(input):
    evenSum = 0
    for i in input:
        if i % 2 == 0:
            evenSum = evenSum + i
    print("Sum of even numbers : ",evenSum)

def oddlist(input):
    oddSum = 0
    for i in input:
        if i % 2 != 0:
            oddSum = oddSum + i
    print("Sum of odd numbers : ",oddSum)

def main():

    list1 = [1,2,3,4,5,6,7,8,9,10]
    T1 = threading.Thread(target=evenlist, args=(list1,))
    T2 = threading.Thread(target=oddlist, args=(list1,))

    T1.start()
    T2.start()

if __name__ == "__main__":
    main()