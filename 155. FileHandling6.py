import os

def main():
    print("Enter the name of file that you want delete : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")
        os.remove(FileName)
        
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()