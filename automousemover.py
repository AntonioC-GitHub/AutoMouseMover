import pyautogui
from datetime import time
import datetime

pyautogui.FAILSAFE = True

start_time = time(9, 0)  # this is the time the user begins their shift

end_time = time(17, 0)  # this is the time the user ends their shift

current_time = datetime.datetime.now()  # this gets the current time for the user's time zone

current_time_only = current_time.time()  # this turns the users time into just the time parameter which is required


# to compare .time function calls


def main():
    while start_time <= current_time_only <= end_time:
        pyautogui.moveTo(0, 1414, duration=1)
        pyautogui.moveTo(56, 0, duration=1)
        pyautogui.moveTo(56, 5, duration=.25)
        pyautogui.moveTo(560, 114, duration=1)
        pyautogui.moveTo(5, 1, duration=.75)

    if current_time_only > end_time:
        print("You are currently not at work")

    if current_time_only < start_time:
        print("You are currently not at work")


if __name__ == '__main__':
    main()
