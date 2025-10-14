import threading

def Display(value1, value2):
    print("Inside display ",value1, value2)

def main():
    print("Inside main")
    T1 = threading.Thread(target = Display, args = (11,21))
    T1.start()
    
if __name__ == "__main__":
    main()