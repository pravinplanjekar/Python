import os
import hashlib

def CalculateChecksum(path):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(100)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(100)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter file name : ")
    filename  = input()

    ret = CalculateChecksum(filename)

    print("Checksum of file is : ",ret)
    
if __name__ == "__main__":
    main()