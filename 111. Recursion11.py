# Input : 4
# Output : 10   (4+3+2+1)

sum = 0

def Add(no):
    global sum

    if(no >= 1):
        sum = sum + no
        no = no - 1
        Add(no)
        
    return sum

def main():
    ret = Add(4)
    print(ret)

if __name__ == "__main__":
    main()
    