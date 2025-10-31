import os
import hashlib

def main():
    print("Enter file name : ")
    filename  = input()

    fobj = open(filename,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(100)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(100)

    fobj.close()

    print("Checksum of file is : ",hobj.hexdigest())

if __name__ == "__main__":
    main()