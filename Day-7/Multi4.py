import threading


def Display():
    print("Inside display")

def main():
    print("Inside main")
    T1 = threading.Thread(target=Display)
    T1.start()

if __name__ == "__main__":
    main()