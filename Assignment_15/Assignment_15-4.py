"""
4. WAP which accept two file names from user and compare contents of both the files. If both the files
contatins same contents then display success otherwise display failure.
Accept names of both the files from command line.

Input: Demo.txt     Hello.txt
Compare contents of Demo.txt and Hello.txt
"""
import sys
import hashlib

"""
Algorithms to calculate checksum MD5, SHA-1, SHA-256 and SHA-512

MD5: 
    - Produces a 128-bit hash value. While still useful for some non-cryptographic uses, it has known 
    vulnerabilities and is not recommended for security-sensitive applications.
SHA-1:
    - Produces a 160-bit hash value. It is also considered weak and should be avoided.

SHA-256:
    - Produces a 256-bit hash value. A strong and widely used algorithm for data integrity checks.

SHA-512:
    - Produces a 512-bit hash value. Another strong algorithm, often a good choice for maximum security.
"""
def calculateChecksum(fileName, hashAlgorithm="md5"):
    hashObj = hashlib.new(hashAlgorithm)
    with open(fileName, 'rb') as fobj:
        buffer = fobj.read(1024)
        while buffer:
            hashObj.update(buffer)
            buffer = fobj.read(1024)
    fobj.close()
    print(f"Filename: {fileName}\tChecksum: {hashObj.hexdigest()}")
    return hashObj.hexdigest()

def compareFileChecksum(fileName1, fileName2):
    checksum1 = calculateChecksum(fileName=fileName1)
    checksum2 = calculateChecksum(fileName=fileName2)
    if checksum1 == checksum2:
        print("Both files are same")
    else:
        print("Files are not same")

def main():
    # $>python Assignment-15-3.py filename1.txt filename2.txt
    if len(sys.argv) == 2:
        if sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This program is use to check contents of 2 files")
            print("Use given options")
            print("--u or --U : Use to display the usage")
        elif sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Usage of this script")
            print("$python <ProgramName.py> <FileName1> <FileName2>")
            print("Use given options")
            print("--h or --H : Use to display the help")
        else:
            print("Use given options")
            print("--h or --H : Use to display the help")
            print("--u or --U : Use to display the usage")
    elif len(sys.argv) == 3 :
        compareFileChecksum(fileName1=sys.argv[1], fileName2=sys.argv[2])

    else:
        print("Warning: Invalid number of command line arguments")
        print("Use the given options as :")
        print("--h or --H : Use to display the help")
        print("--u or --U : Use to display the usage")

if __name__ == "__main__":
    main()

"""
Output:

visawant@fedora:~/Desktop/Python_Marvellous/Assignment_15$ python Assignment_15-4.py Assignment_15-3.py Demo.txt 
Filename: Assignment_15-3.py	Checksum: 764fcdfe84b5a2f01fe5eb2ee5015c93
Filename: Demo.txt	Checksum: f85225ea53629b08dd923fc004c968b9
Files are not same

visawant@fedora:~/Desktop/Python_Marvellous/Assignment_15$ python Assignment_15-4.py Demo1.txt Demo.txt 
Filename: Demo1.txt	Checksum: f85225ea53629b08dd923fc004c968b9
Filename: Demo.txt	Checksum: f85225ea53629b08dd923fc004c968b9
Both files are same


"""