# use of schedule module in python, updated copy of Automation3.py
import schedule
import time
import datetime

def MySchedule():
    print("Inside MySchedule function at :",datetime.datetime.now())

def main():
    print("-- Inside automation script --")
    print("Current time is :",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("Application is in waiting state :")
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("End of automation script")

if __name__ == "__main__":
    main()