# Input : 4
# Output : *    *   *   *

def Display(no):
    while(no >= 1):
        print("*",end=" ")
        no = no - 1

    print()

def main():
    Display(4)

if __name__ == "__main__":
    main()
    