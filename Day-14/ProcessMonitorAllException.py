import psutil

def ProcessDisplay():
    Boarder = "*"*50
    print(Boarder)
    print("Information of currently running processes : ")
    print(Boarder)

    for proc in psutil.process_iter():
        try:
            # Get the output of proc in dictionary format
            info = proc.as_dict(attrs=['pid','name','username'])

            # add new key 'vms' in the exisiting info dictionary
            info['vms'] = proc.memory_info().vms / (1024 * 1024)    # give info in MB
            print(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(e)


def main():
    ProcessDisplay()

if __name__ == "__main__":
    main()