def main():
    print("Enter total marks : ")
    value1 = int(input())

    print("Enter obtained marks : ")
    value2 = int(input())

    output = ((value2 / value1) * 100)

    print("Percentage is : ",output)

if __name__ == "__main__":
    main()