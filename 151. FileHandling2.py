def main():
    print("Enter the name of file that you want to create : ")
    FileName = input()

    fobj = open(FileName, "x")

if __name__ == "__main__":
    main()