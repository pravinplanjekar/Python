def Display(*A):
    print(type(A))
    print("Inside Display",A)
    
def main():
    Display(11,21,51,101)
    Display(11,21,51,101,111)
    Display(11,21,51)
    Display(11)
    Display()


if __name__ == "__main__":
    main()