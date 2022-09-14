from datetime import datetime, timedelta
import time
from playsound import playsound
import logging

MINUTES = 1

def pomodoro(minutes):
    try:
        startDate = datetime.now()
        
        endDate = startDate + timedelta(minutes=minutes)
        currentTime = startDate.strftime("%H:%M:%S")
        endTime = endDate.strftime("%H:%M:%S")
        while currentTime != endTime:
            date = datetime.now()
            currentTime = date.strftime("%H:%M:%S")
            time.sleep(1)

        playsound("bell.mp3")
    except:
        logging.exception("Exception in pomodoro()")
        raise
    return startDate

print("Welcome to the pomodoro timer")
print("-----------------------------")
MINUTES = int(input("How many minutes is your timer: "))
end = False
times = 0
while end != True:
    input("Press enter to start a cycle \n")
    pomodoro(MINUTES)
    times += 1
    timeWorked = MINUTES * times

    print("You have completed {0} pomodoro".format(times))
    print("Total time worked: {0} Minutes \n".format(timeWorked))