import os

def main():
    print("Enter the name of file that you want read : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")
        fobj = open(FileName,"r")
        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()

    else:
        print("There is no such file")

if __name__ == "__main__":
    main()