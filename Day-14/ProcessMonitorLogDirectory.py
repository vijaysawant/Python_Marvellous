import os
import psutil
import time

def CreateLog(FolerName, Data):
    if not os.path.exists(FolerName):
        os.mkdir(FolerName)
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolerName,"Marvellous_%s.log"%{timestamp})
    fobj = open(FileName,"w")
    Boarder = "-"*80
    fobj.write(Boarder)
    fobj.write("\n\tMarvellous Infosystems Process Log\n")
    fobj.write("\tLog file is created at: "+time.ctime()+"\n")
    fobj.write(Boarder+"\n")

    for value in Data:
        fobj.write(f"{value}\n\n")
    fobj.write(Boarder)

    fobj.close()


def ProcessScan():
    listProcess = []

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
            listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(e)
    return listProcess


def main():
    retValList = ProcessScan()
    CreateLog("MarvellousProcess",retValList)

if __name__ == "__main__":
    main()