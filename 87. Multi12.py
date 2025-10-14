import os

def fun(no):
    sum = 0
    for i in range(1,no):
        sum = sum + (i*i*i)
    return sum

def main():
    ret = fun(1000)
    print(ret)

if __name__ == "__main__":
    main()