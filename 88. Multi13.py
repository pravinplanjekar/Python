import os
import time

def fun(no):
    print("PID is : ",os.getpid())
    sum = 0
    for i in range(1,no):
        sum = sum + (i*i*i)
    return sum

def main():
    start_time = time.time()

    data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    result = []

    for i in data:
        result.append(fun(i))
    
    print(result)

    end_time = time.time()

    print("Execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()