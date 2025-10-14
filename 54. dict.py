#dict

# syntax : { key : value}
# hetero
# ordered
# indexed (not numeric)
# key duplicate allowed but old gets overwitten
# value duplicate allowed
# data mutable (value)


data = {"Name" : "Let us C", "Author" : "Y kanetkar", "Price" : 340, "Publication": "BPB Publication"}

print("data type : ",type(data))
print("Length is : ",len(data))
print(data)

print(data["Author"])

data["Price"] = 400
print(data)

