
def main():
    Ans = 0

    try:
        print("Enter first number : ")
        no1 = int(input())

        print("Enter second number : ")
        no2 = int(input())

        Ans = no1 / no2

    except ZeroDivisionError as zobj:
        print("Exception ocurred due to second input : ",zobj)
        
    except ValueError as vobj:
        print("Invalid data type of input : ",vobj)

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()