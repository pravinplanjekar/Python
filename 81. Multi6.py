import threading

def Display(value1, value2):
    print("Inside display ",value1, value2)
    for i in range(1000):
        print(i)

def main():
    print("Inside main")
    T1 = threading.Thread(target = Display, args = (11,21))
    T1.start()
    print("End of main")
    
if __name__ == "__main__":
    main()