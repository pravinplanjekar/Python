def CheckEven(No):
    return (No % 2 == 0)

ret = CheckEven(11)

if ret == True:
    print("Number is even")
else:
    print("Number is odd")