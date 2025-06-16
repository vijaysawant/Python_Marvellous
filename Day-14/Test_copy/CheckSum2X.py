import os
import hashlib  # use to calculate checksum

def CalculateCheckSum(path):
    fobj = open(path, 'rb')     # open file in read byte mode

    hobj = hashlib.md5()

    buffer = fobj.read(100)        # read 100 bytes
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(100)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter file name: ")
    filename = input()
    ret = CalculateCheckSum(filename)
    print("Checksum of file is: ",ret)

if __name__ == "__main__":
    main()