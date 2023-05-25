# your code goes here!
import time


def countdown(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        if num == 1:
            print("HAPPY NEW YEAR!")
        num -= 1


def countdown_with_sleep(num):
    while num > 0:
        print(f"{num} SECOND(S)!")
        if num == 1:
            print("HAPPY NEW YEAR!")
        time.sleep(1)
        num -= 1


countdown_with_sleep(10)
