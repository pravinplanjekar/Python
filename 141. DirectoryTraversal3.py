import os

def DirectoryWatcher(DirectoryName):
    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub Folder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)

def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()