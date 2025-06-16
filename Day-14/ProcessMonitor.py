import psutil

def ProcessDisplay():
    Boarder = "*"*50
    print(Boarder)
    print("Information of currently running processes : ")
    print(Boarder)

    for proc in psutil.process_iter():
        # Get the output of proc in dictionary format
        info = proc.as_dict(attrs=['pid','name'])
        print(info)


def main():
    ProcessDisplay()

if __name__ == "__main__":
    main()