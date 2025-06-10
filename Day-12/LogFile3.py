# This script is Create a log file which has time stamp in it.
import sys
import time

def CreateLog():
    timestamp = time.ctime()
    filename = "MarvellousLog_%s.log"%(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,"w")

    Border = "-"*50
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write(Border+"\n")

    fobj.write("\n"*10)
    fobj.write(Border+"\n")
    fobj.write("File created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

def main():
    CreateLog()

if __name__ == "__main__":
    main()