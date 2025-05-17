import threading

def Display(value1, value2):
    print("Inside display ",value1, value2)
    print("Thread ID of child thread (Display) is : ",threading.get_ident())
    for i in range(10):
        print(i)

def main():
    print("Inside main")
    print("Thread ID of main is : ",threading.get_ident())
    T1 = threading.Thread(target=Display, args= (11,21))
    T1.start()
    T1.join()   # join method force main thread to wait untill child thread executes
    print("End of main")

if __name__ == "__main__":
    main()