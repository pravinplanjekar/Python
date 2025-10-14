import threading
import time

def SumEven(no):
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    print(sum)

def SumOdd(no):
    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i
    print(sum)

def main():
    print("Demonstration of serial execution")

    start_time = time.time()

    SumEven(900000000)
    SumOdd(900000000)

    end_time = time.time()

    print("Time requred for execution is : ",end_time - start_time)

    print("end of main")

if __name__ == "__main__":
    main()