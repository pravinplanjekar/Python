def Increase(A):
    return A+1

def Demo(Task, Value):
    for no in Value:
        print(Task(no))
    
Data = [13,17,10,14,11]

Demo(Increase, Data)