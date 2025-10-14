def CalculatePercentage(Total, Obtained):
    output = ((Obtained / Total) * 100)
    return output

def main():
    print("Enter total marks : ")
    value1 = int(input())

    print("Enter obtained marks : ")
    value2 = int(input())

    result = CalculatePercentage(Obtained=value2, Total=value1) # keyword arguments

    print("Percentage is : ",result)

if __name__ == "__main__":
    main()