import psutil

def KillProcess(ProcessName):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == ProcessName:
            print("Killing the process: ",ProcessName)
            proc.kill()

def main():
    KillProcess("gnome-calculator")
    KillProcess("firefox")

if __name__ == "__main__":
    main()