import os
import json
from time import sleep
from collections import OrderedDict

MIN_USERNAMEPASS_LENGTH = 4
MAX_USERNAMEPASS_LENGTH = 16
money = 0
logged_account = ""


def save_account():
    with open("accounts.json", "w") as file:
        json.dump(accountlist, file)


def save_username():
    with open("usernames.json", "w") as file:
        json.dump(usernamelist, file)


def save_password():
    with open("passwords.json", "w") as file:
        json.dump(passwordlist, file)


def get_accounts():
    file = open("accounts.json")
    accountlist = json.load(file)


def get_usernames():
    file = open("usernames.json")
    usernamelist = json.load(file)


def get_passwords():
    file = open("passwords.json")
    passwordlist = json.load(file)


def create_acc():
    while True:
        username = input("What would you like your username to be? (4-16 characters) ")
        if MIN_USERNAMEPASS_LENGTH <= len(username) <= MAX_USERNAMEPASS_LENGTH:
            if username in usernamelist:
                print("This username is already taken!")
            else:
                if len(usernamelist) == len(passwordlist):
                    usernamelistlength = len(usernamelist) + 1
                    usernamelist.insert(-1, username)
                    save_username()
                    print("Username saved!")
                    break
                else:
                    print("Something is wrong with the saved usernames and passwords. Aborting!")
                    sleep(1)
                    quit()
        else:
            print("Your username must be between 4-16 characters.")
    while True:
        password = input("What would you like your password to be? (4-16 characters) ")
        if MIN_USERNAMEPASS_LENGTH <= len(password) <= MAX_USERNAMEPASS_LENGTH:
            passwordlistlength = len(passwordlist) + 1
            passwordlist.insert(-1, password)
            accountlist[str(usernamelistlength)] = {"username": username, "password": password}
            with open("accounts.json", "w") as file:
                json.dump(accountlist, file)
            with open("passwords.json", "w") as file:
                json.dump(passwordlist, file)
            print("Password saved and account created!")
            break
        else:
            print("Your password must be between 4-16 characters.")


def login():
    while True:
        loginusername = input("Username: ")
        if loginusername in usernamelist:
            print(f"Found account {loginusername}!")
            break
        else:
            print("Could not find an account for this username!")
    while True:
        loginpassword = input("Password: ")
        if loginpassword in passwordlist:
            logged_account = loginusername
            print(f"Logged in to {loginusername}!")
            break
        else:
            print("Wrong password!")


def listusernames():
    for key in accountlist.items():
        print(key)
# sdouifgh

file = open("accounts.json")
accountlist = json.load(file)
file = open("usernames.json")
usernamelist = json.load(file)
file = open("passwords.json")
passwordlist = json.load(file)
while True:
    sign_in = input(
        "Welcome to the game!\nYou are currently not signed in.\nWould you like to log in, create an account, "
        "or list the current account usernames?"
        "(Options: Login, Create, List) ")
    if sign_in.lower() == "list":
        print(usernamelist)
    if sign_in.lower() == "create":
        create_acc()
    if sign_in.lower() == "login":
        get_usernames()
        get_passwords()
        login()
        break
