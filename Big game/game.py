import os
import json
from time import sleep

MIN_USERNAMEPASS_LENGTH = 4
MAX_USERNAMEPASS_LENGTH = 16
accountlist = {}
money = 0
logged_account = ""


def save_accs():
    with open('accounts.json', 'w') as file:
        json.dump(accountlist, file)


def get_accs():
    file = open("accounts.json")
    accountlist = json.load(file)


def create_acc():
    while True:
        username = input("What would you like your username to be? (4-16 characters) ")
        if MIN_USERNAMEPASS_LENGTH <= len(username) <= MAX_USERNAMEPASS_LENGTH:
            if username in accountlist:
                print("This username is already taken!")
            else:
                print("Username saved!")
                break
        else:
            print("Your username must be between 4-16 characters.")
    while True:
        password = input("What would you like your password to be? (4-16 characters) ")
        if MIN_USERNAMEPASS_LENGTH <= len(password) <= MAX_USERNAMEPASS_LENGTH:
            print("Saved password and created account!")
            accountlist[username] = {password: money}
            save_accs()
            print("Now you can log into your account!")
            break
        else:
            print("Your password must be between 4-16 characters.")


def login():
    while True:
        loginusername = input("Username: ")
        if loginusername in accountlist:
            print(f"Found account {loginusername}!")
            break
        else:
            print("Could not find an account for this username!")
    while True:
        loginpassword = input("Password: ")
        if loginpassword in accountlist:
            logged_account = loginusername
            print(f"Logged in to {loginusername}")


get_accs()
while True:
    sign_in = input(
        "Welcome to the game!\nYou are currently not signed in.\nWould you like to log in or create an account?"
        "(Options: Login, Create) ")
    if sign_in.lower() == "create":
        create_acc()
    if sign_in.lower() == "login":
        login()
        break
