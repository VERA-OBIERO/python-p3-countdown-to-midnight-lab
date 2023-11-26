# your code goes here!
import time

def countdown(x):
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        time.sleep(1) 
        seconds -= 1
    print("HAPPY NEW YEAR!")