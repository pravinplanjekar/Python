def CalculatePercentage(Obtained, Total = 500):
    output = ((Obtained / Total) * 100)
    return output

def main():
    print("Enter obtained marks : ")
    value2 = int(input())

    result = CalculatePercentage(value2) 

    print("Percentage is : ",result)

if __name__ == "__main__":
    main()