def main():
    print("Enter number of elements : ")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered elements are : ")
    for value in Data:
        print(value)

if __name__ == "__main__":
    main()