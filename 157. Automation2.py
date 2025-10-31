import schedule
import time
import datetime

def MySchedule():
    print("Inside MySchecule function at : ",datetime.datetime.now())

def main():
    print("Inside automation script")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("End of automation script")
    
if __name__ == "__main__":
    main()