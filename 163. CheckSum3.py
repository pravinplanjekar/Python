import hashlib

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter file name : ")
    filename  = input()

    ret = CalculateChecksum(filename)

    print("Checksum of file is : ",ret)
    
if __name__ == "__main__":
    main()