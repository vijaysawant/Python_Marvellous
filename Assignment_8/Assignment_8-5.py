"""
5. Design python application which contains two threads named as thread1 and thread2. Thread1 display
1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. After execution of thread1
gets completed then schedule thread2.
"""
import threading

def DisplayNormal():
    print("Printing in normal order ")
    for i in range(1, 51, 1):
        print(i)

def DisplayReverse():
    print("Printing in reverse order ")
    for i in range(50, 0, -1):
        print(i)

def main():
    thread1 = threading.Thread(target=DisplayNormal)
    thread2 = threading.Thread(target=DisplayReverse)

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()