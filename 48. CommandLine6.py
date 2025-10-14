def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    
    Result = Addition(value1, value2)

    print("Addition is : ",Result)

if __name__ == "__main__":
    main()
    