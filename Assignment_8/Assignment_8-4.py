"""
4. Design python application which creates three threads as small, capital, digits. All the threads accepts
string as parameter. Small thread display number of small characters, capital thread display number of 
capital characters and digits thread display number of digits. Display id and name of each thread.
"""
import os
import threading

def small(inputStr):
    smallThreadId = threading.get_ident()
    print("\n----> small thread id : ",smallThreadId)
    for i in inputStr:
        if i >= 'a' and i <= 'z':
            print("Small : ",i)

def capital(inputStr):
    capitalThreadId = threading.get_ident()
    print("\n----> Capital thread id : ",capitalThreadId)
    for i in inputStr:
        if i >= 'A' and i <= 'Z':
            print("Capital : ",i)

def digits(inputStr):
    digitsThreadId = threading.get_ident()
    print("\n----> digits thread id : ",digitsThreadId)
    for i in inputStr:
        if i >= '0' and i <= '9':
            print("Digits : ",i)

def main():
    inputStr = "123ABCpqr$XYZlmn456"

    MainThreadId = os.getpid()
    print("--> Main thread id : ",MainThreadId)
    print("Input String : ",inputStr,end="\n")

    threading.current_thread()
    T1 = threading.Thread(target=small, args=(inputStr,))
    T2 = threading.Thread(target=capital, args=(inputStr,))
    T3 = threading.Thread(target=digits, args=(inputStr,))

    T1.start()
    T1.join()
    
    T2.start()
    T2.join()

    T3.start()
    T3.join()

if __name__ == "__main__":
    main()

"""
Note: If we don't use 'T1.join()' then output may change as per schedular, there are 2 such output scenarios 
attached in the file which don't uses join() method.
join() waits until current thread executes

Output: 

vijay@fedora:~/Desktop/Python_Marvellous/Assignment_8$ python Assignment_8-4.py 
--> Main thread id :  82381
Input String :  123ABCpqr$XYZlmn456

----> small thread id :  139716876826304
Small :  p
Small :  q
Small :  r
Small :  l
Small :  m
Small :  n

----> Capital thread id :  139716868433600
Capital :  A
Capital :  B
Capital :  C
Capital :  X
Capital :  Y
Capital :  Z

----> digits thread id :  139716868433600
Digits :  1
Digits :  2
Digits :  3
Digits :  4
Digits :  5
Digits :  6


vijay@fedora:~/Desktop/Python_Marvellous/Assignment_8$ python Assignment_8-4.py 
--> Main thread id :  82464
Input String :  123ABCpqr$XYZlmn456

----> small thread id :  140091490686656
Small :  p
Small :  q
Small :  r
Small :  l
Small :  m
Small :  n

----> Capital thread id :  140091482293952

----> digits thread id :  140091490686656
Capital :  A
Digits :  1
Capital :  B
Capital :  C
Capital :  X
Digits :  2
Capital :  Y
Digits :  3
Capital :  Z
Digits :  4
Digits :  5
Digits :  6


"""