from time import *
import random as r


def mistake(paragraph, userInput):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != userInput[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(start_time, end_time, textInput):
    time_delay = end_time - start_time
    time_roundoff = round(time_delay, 2)
    speed = len(textInput) / time_roundoff
    return round(speed)


while True:
    check=input("Ready to test:y/n ? ")
    if check=="y":
        test = [
            "The quick brown fox jumps over the lazy dog",
            "I love programming in Python",
            "Welcome to my github repository",
        ]

        test1 = r.choice(test)
        print("---------- Typing Speed ---------- ")
        print(test1)
        print()
        start_time = time()
        textInput = input("Enter : ")
        end_time = time()
        print(f"Speed:  {speed_time(start_time, end_time,textInput)} w/sec")
        print(f"Error: {mistake(test1,textInput)}")
    elif check=="n":
        print("Thank You!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")