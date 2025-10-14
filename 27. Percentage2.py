def CalculatePercentage(Total, Obtained):
    output = ((Obtained / Total) * 100)
    return output

def main():
    print("Enter total marks : ")
    value1 = int(input())

    print("Enter obtained marks : ")
    value2 = int(input())

    result = CalculatePercentage(value1,value2)

    print("Percentage is : ",result)

if __name__ == "__main__":
    main()