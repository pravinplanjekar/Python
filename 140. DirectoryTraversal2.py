import os

def DirectoryWatcher():
    for FolderName , SubFolderNames, FileNames in os.walk("Marvellous"):
        print("Folder name is : "+FolderName)

        for subf in SubFolderNames:
            print("Sub Folder name is : "+subf)

        for fname in FileNames:
            print("File name is : "+fname)

def main():
    DirectoryWatcher()

if __name__ == "__main__":
    main()