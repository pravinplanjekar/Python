def Increase(A):
    return A+1

def Demo(Task, Value):
    Result = []

    for no in Value:
        ret = Task(no)
        Result.append(ret)

    return Result
    
Data = [13,17,10,14,11]

Rdata = list(Demo(Increase, Data))

print(Rdata)