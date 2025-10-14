def Multiplication(Value1, Value2):
    result = Value1 * Value2
    return result

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ans = Multiplication(no1, no2)

    print("Multiplication is : ",ans)

if __name__ == "__main__":
    main()