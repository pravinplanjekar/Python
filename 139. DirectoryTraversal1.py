import os

def main():
    for FolderName , SubFolderNames, FileNames in os.walk("Marvellous"):
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub Folder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)

if __name__ == "__main__":
    main()