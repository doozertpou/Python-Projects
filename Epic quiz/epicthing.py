import os
import math
from time import sleep

from playsound import playsound


def countdown():
    os.system("cls")
    countdowntime = 5
    while countdowntime >= 1:
        print("Moving on to the next question in: " + str(countdowntime) + "...")
        sleep(1)
        countdowntime = countdowntime - 1
        os.system("cls")


print("Press any key to start the quiz!")
os.system("pause")

os.system("cls")
print("Doozer's epic quiz!\nAnswer all of the questions right!\n")
answer1 = input("Question 1:\nWhat is 4 + 7? ")
if answer1 != "11":
    print("\nWrong, try again next time!\n")
    action = input("Options: Try again! (r), Quit. (q)\nWhat do you want to do "
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
    os.system("cls")
    answer2 = input("Question 2:\nWhat is 17 - 6? ")
    if answer2 != "11":
        print("\nWrong, try again next time!\n")
        action = input(
            "Options: Try again! (r), Quit. (q)\nWhat do you want to do now? ")
        if action.lower() == "q":
            quit()
        if action.lower() == "r":
            exec(open("epicthing.py").read())
    else:
        os.system("cls")
        print("Correct!")
        countdown()
        answer3 = input("Question 3:\nIf Billy has 764 apples,\nand he eats 753 of them,\nhow many are left? ")
        if answer3 != "11":
            print("\nWrong, try again next time!\n")
            action = input(
                "Options: Try again! (r), Quit. (q)\nWhat do you want to do now? ")
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
                    "Options: Try again! (r), Quit. (q)\nWhat do you want to do "
                    "now? ")
                if action.lower() == "q":
                    quit()
                if action.lower() == "r":
                    exec(open("epicthing.py").read())
            else:
                os.system("cls")
                print("Correct!")
                countdown()

            os.system("cls")
            print("Question 5:\nThis one is the hardest of all")
            sleep(1)
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
                    "Options: Try again! (r), Quit. (q)\nWhat do you want to do "
                    "now? ")
                if action.lower() == "q":
                    quit()
                if action.lower() == "r":
                    exec(open("epicthing.py").read())
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
                os.system("pause")
