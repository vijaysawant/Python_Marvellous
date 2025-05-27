"""
1. Design python application which creates two threads named as even and odd. Even thread will display
first 10 even numbers and odd thread will display first 10 odd numbers.
"""
import threading

def Even():
    """This thread will display first 10 even numbers"""
    print(f"\n--Inside {Even.__name__} Thread--")
    for i in range(0,20,2):
        print(f"Even :",i)

def Odd():
    """This thread will display first 10 odd numbers"""
    print(f"\n--Inside {Odd.__name__} Thread--")
    for i in range(1,20,2):
        print("Odd : ",i)

def main():
    print(f"--Inside {main.__name__} function--")
    T1 = threading.Thread(target=Even)
    T2 = threading.Thread(target=Odd)

    T1.start()
    T2.start()

if __name__ == "__main__":
    main()