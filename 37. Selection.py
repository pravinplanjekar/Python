def main():
    print("Enter your age")
    Age = int(input())

    if(Age < 18):
        print("You cant paricipate in voting")
    else:
        print("You can participate in voting")
        
if __name__ == "__main__":
    main()