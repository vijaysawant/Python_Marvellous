import os
import hashlib  # use to calculate checksum

def main():
    print("Enter file name: ")
    filename = input()

    fobj = open(filename, 'rb')     # open file in read byte mode

    hobj = hashlib.md5()

    buffer = fobj.read(1024)        # read 1024 bytes/1 kb data
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    print("Checksum of file is: ",hobj.hexdigest())

if __name__ == "__main__":
    main()