def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

ret = CheckEven(10)

if ret == True:
    print("Number is even")
else:
    print("Number is odd")