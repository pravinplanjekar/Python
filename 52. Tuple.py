# Tuple

# Syntax : ()
# heter
# ordered
# index
# data immutable
# tuple immutable
# duplicate

data = (10,"Hello",90.67,True,10)

print("Data type is : ",type(data))
print("Length is : ",len(data))
print(data)

print(data[0])
print(data[1])

# data[0] = 11

print("Data using loop")
for value in data:
    print(value)

for i in range(len(data)):
    print(data[i])