import os
import sys
import time
import hashlib
import schedule

def CalculateCheckSum(path, BlockSize=1024):
    fobj = open(path, 'rb')     # open file in read byte mode

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)        # read 1024 bytes
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

# def DirectoryWatcher(DirectoryName = "Marvellous"):

#     flag = os.path.isabs(DirectoryName)     # check path is absolute path or not
#     # if directory path is not absolute path then convert it into absolute path
#     if flag == False:
#         DirectoryName = os.path.abspath(DirectoryName)  # Convert path to absolute path

#     flag = os.path.exists(DirectoryName)
#     # if Directory path does not exists then exit from code
#     if flag == False:
#         print("The path is invalid")
#         exit()

#     flag = os.path.isdir(DirectoryName)
#     # if directory is not a directory then exit from code
#     if flag == False:
#         print("Path is valid but target is not directory")
#         exit()


#     for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
#         for fname in FileNames:
#             fname = os.path.join(FolderName,fname)
#             checksum = CalculateCheckSum(fname)
#             print("File Name: ",fname)
#             print("Checksum : ",checksum)
#             print()

    # # Log
    # timestamp = time.ctime()
    # filename = "MarvellousLog_%s.log"%(timestamp)
    # filename = filename.replace(" ","_")
    # filename = filename.replace(":","_")

    # fobj = open(filename,"w")

    # Border = "-"*50
    # fobj.write(Border+"\n")
    # fobj.write("This is a log file of Marvellous Automation Script\n")
    # fobj.write("This is a Directory Script\n")
    # fobj.write(Border+"\n")

    # fobj.write(Border+"\n")
    # fobj.write("File created at : "+timestamp+"\n")
    # fobj.write(Border+"\n")

def FindDuplicateFiles(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)     # check path is absolute path or not
    # if directory path is not absolute path then convert it into absolute path
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)  # Convert path to absolute path

    flag = os.path.exists(DirectoryName)
    # if Directory path does not exists then exit from code
    if flag == False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    # if directory is not a directory then exit from code
    if flag == False:
        print("Path is valid but target is not directory")
        exit()

    DuplicateDict = {}      # This dictionary is use to store checksum and file path

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)

            if checksum in DuplicateDict:
                DuplicateDict[checksum].append(fname)
            else:
                DuplicateDict[checksum] = [fname]

    return DuplicateDict

# DisplayResult() is just to display DuplicateDict which contains file paths
def DisplayResult(MyDict):
    result = list(filter(lambda X: len(X)> 1, MyDict.values()))
    count = 0    
    for file_paths in result:
        for file_path in file_paths:
            count = count + 1
            print(file_path)
        print("--------------------------")
        print("Value of count is: ",count)
        print("--------------------------")
        count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicateFiles(Path)
    result = list(filter(lambda X: len(X)> 1, MyDict.values()))
    count = 0
    TotalDelete = 0
    for file_paths in result:
        for file_path in file_paths:
            count = count + 1
            # remove file if it is greate than one
            if count > 1:
                TotalDelete = TotalDelete + 1
                print("Deleting file : ",file_path)
                os.remove(file_path)
        count = 0
    print("Total Deleted Files: ",TotalDelete)

def main():
    Border = "-"*50
    print(Border)
    print("---------- Marvellous Automation ----------")
    print(Border)
    print()

    if len(sys.argv) == 3:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform Directory cleaning")
            print("This is the directory automation script")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory TimeInterval")
            print("Please provide valid absolute path")

        else:
            # result = FindDuplicateFiles(sys.argv[1])
            # DisplayResult(result)
            # DeleteDuplicate(result)
            schedule.every(1).minutes.do(DeleteDuplicate)
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Warning: Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Use to display the help")
        print("--u : Use to display the usage")

    print()
    print(Border)
    print("------- Thank you for using script -------")
    print("--------- Marvellous Infosystems ---------")
    print(Border)


if __name__ == "__main__":
    main()