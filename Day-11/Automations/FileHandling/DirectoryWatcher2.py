# Program to 

import os

def main():
    print("Enter the name of Directory : ")
    DirName = input()

    ret = os.path.isabs(DirName)
    
    if (ret == True):
        print("Input is absolute path")

    else:
        print("Input is Relative path")
        NewPath = os.path.abspath(DirName)
        print("Updated path is : ",NewPath)

if __name__ == "__main__":
    main()


"""
Input: 
Relative path - Day-11/Automations/FileHandling
Absolute path - /home/visawant/Desktop/Python_Marvellous/Day-11/Automations/FileHandling

Output:

visawant@fedora:~/Desktop/Python_Marvellous/Day-11/Automations/FileHandling$ python DirectoryWatcher.py 
Enter the name of Directory : 
FileHandling
Input is not absolute path

visawant@fedora:~/Desktop/Python_Marvellous/Day-11/Automations/FileHandling$ python DirectoryWatcher.py 
Enter the name of Directory : 
/home/visawant/Desktop/Python_Marvellous/Day-11/Automations/FileHandling
Input is absolute path

"""