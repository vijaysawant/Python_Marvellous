# This program is to travel "Marvellous" directory, here we validate file path, existance and its status,
# is it directory or not
# delete only empty files
import os

def DirectoryWatcher(DirectoryName = "Marvellous"):

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

    print("Absolute path is : ",DirectoryName)

    TotalCount = 0
    EmptyCount = 0

    for FolerName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            TotalCount = TotalCount + 1
            if os.path.getsize(os.path.join(FolerName,fname)) == 0:
                EmptyCount = EmptyCount + 1
                print("File Name : ",fname)
                print("Removed file :",os.path.join(FolerName,fname))
                os.remove(os.path.join(FolerName,fname))
    
    print("Total Number of files scanned : ",TotalCount)
    print("Total Number of empty files : ", EmptyCount)

def main():
    print("Enter name of directory that you want to travel : ")
    DirName = input()
    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()