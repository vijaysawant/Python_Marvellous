"""
5. Accept file name and one string from user and return the frequency of that string from file.

Input: Demo.txt     Marvellous
Search "Marvellous" in Demo.txt
"""
import sys

def checkWordOccuranceInFile(fileName, word=""):
    count = 0
    # import ipdb; ipdb.set_trace()
    with open(file=fileName, mode='r') as fobj:
        buffer = fobj.readline()
        while buffer:
            for ListOfWords in [buffer.split(" ")]:
                for singleword in ListOfWords:
                    if word in singleword:
                        count = count + 1
            buffer = fobj.readline()
    fobj.close()
    print(f"'{word}' occurs {count} times")

def main():
    # $>python Assignment-15-3.py filename1.txt wordToCheckOccurance
    if len(sys.argv) == 2:
        if sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This program is use to check contents of 2 files")
            print("Use given options")
            print("--u or --U : Use to display the usage")
        elif sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this script")
            print("$python <ProgramName.py> <FileName1> <wordToCheckOccurance>")
            print("Use given options")
            print("--h or --H : Use to display the help")
        else:
            print("Use given options")
            print("--h or --H : Use to display the help")
            print("--u or --U : Use to display the usage")
    elif len(sys.argv) == 3 :
        checkWordOccuranceInFile(fileName=sys.argv[1], word=sys.argv[2])

    else:
        print("Warning: Invalid number of command line arguments")
        print("Use the given options as :")
        print("--h or --H : Use to display the help")
        print("--u or --U : Use to display the usage")

if __name__ == "__main__":
    main()