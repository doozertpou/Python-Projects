import os
import math
from threading import Thread
from time import sleep

from playsound import playsound


def play_careful():
    playsound("CAREFUL.mp3", True)


def countdown():
    os.system("cls")
    countdowntime = 5
    while countdowntime >= 1:
        print("Moving on to the next question in: " + str(countdowntime) + "...")
        sleep(1)
        countdowntime = countdowntime - 1
        os.system("cls")


print("any key to start")
os.system("pause")


song1 = Thread(target=play_careful)
song1.start()
print("epic intro (pls pretend its cool so jeremy feels good)")
sleep(11)

os.system("cls")
print("Jeremy's epic quiz!\nAnswer all of the questions right!\n")
answer1 = input("Question 1:\nWhat is 4 + 7? ")
if answer1 != "11":
    print("\nWrong, try again next time!\n")
    action = input("Options: Try again! (r), q and let Jeremy punch you >:) (q)\nWhat do you want to do "
                   "now? ")
    if action.lower() == "q":
        quit()
    if action.lower() == "r":
        exec(open("epicthing.py").read())

else:
    os.system("cls")
    print("Correct!")
    sleep(1)
    countdown()
    song1 = Thread(target=play_careful)
    song1.start()
    os.system("cls")
    song1 = Thread(target=play_careful)
    song1.start()
    answer2 = input("Question 2:\nWhat is 17 - 6? ")
    if answer2 != "11":
        print("\nWrong, try again next time!\n")
        action = input(
            "Options: Try again! (r), q and let Jeremy punch you >:) (q)\nWhat do you want to do now? ")
        if action.lower() == "q":
            quit()
        if action.lower() == "r":
            exec(open("epicthing.py").read())
    else:
        os.system("cls")
        print("Correct!")
        countdown()
        song1 = Thread(target=play_careful)
        song1.start()
        answer3 = input("Question 3:\nIf Billy has 764 apples,\nand he eats 753 of them,\nhow many are left? ")
        if answer3 != "11":
            print("\nWrong, try again next time!\n")
            action = input(
                "Options: Try again! (r), q and let Jeremy punch you >:) (q)\nWhat do you want to do now? ")
            if action.lower() == "q":
                quit()
            if action.lower() == "r":
                exec(open("epicthing.py").read())
        else:
            os.system("cls")
            print("Correct!")
            countdown()

            answer4 = input(
                "Question 4:\nIf I pooped 4 times today, and 3 people died during the\nproduction of this quiz, "
                "whats 10 + 1? ")
            if answer4 != "11":
                print("\nWrong, try again next time!\n")
                action = input(
                    "Options: Try again! (r), q and let Jeremy punch you >:) (q)\nWhat do you want to do "
                    "now? ")
                if action.lower() == "q":
                    quit()
                if action.lower() == "r":
                    exec(open("epicthing.py").read())
            else:
                song1 = Thread(target=play_careful)
                song1.start()
                os.system("cls")
                print("Correct!")
                countdown()

            os.system("cls")
            print("Question 5:\nThis one is the hardest of all")
            sleep(1)
            song1 = Thread(target=play_careful)
            song1.start()
            os.system("cls")
            print("Question 5:\nThis one is the hardest of all.")
            sleep(1)
            os.system("cls")
            print("Question 5:\nThis one is the hardest of all..")
            sleep(1)
            os.system("cls")
            print("Question 5:\nThis one is the hardest of all...")
            sleep(1)
            os.system("cls")

            answer4 = input("Question 5 (FINAL QUESTION!):\nWhat is the answer to all of these questions? ")
            if answer4 != "11":
                print("\nWrong, try again next time!\n")
                action = input(
                    "Options: Try again! (r), q and let Jeremy punch you >:) (q)\nWhat do you want to do "
                    "now? ")
                if action.lower() == "q":
                    quit()
                if action.lower() == "r":
                    exec(open("epicthing.py").read())
                    song1 = Thread(target=play_careful)
                    song1.start()
            else:
                sleep(3)
                os.system("cls")
                print(".")
                sleep(1)
                os.system("cls")
                print("..")
                sleep(1)
                os.system("cls")
                print("...")
                sleep(1)
                os.system("cls")
                sleep(math.pi)
                print("WRONG!!!!")
                sleep(1)
                print("Just kidding!\nYou got all the questions right, you must be some sort of genius!\n")
                sleep(1)
                print("future jeremy here, its about 10:15 pm the day before you're\ndoing the puzzle, just wanted to "
                      "inform you that i cant stop the songs and\nthe 'press any key to continue' thing is broken,"
                      "\nso you have to sit here for a while.\n\nhave fun!\n")
                os.system("pause")
