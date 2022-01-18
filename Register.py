from email_validator import validate_email, EmailNotValidError
import tkinter as tk
import re

global Email
global Username
global Password
global invalid_input


def main_menu():
    print("Create your account!")
    input_details()


def Email_Validation():  # Validates that the fields the user enters are correct
    global Email
    global invalid_input
    try:
        # Validate.
        valid = validate_email(Email)

        # Update with the normalized form.
        email = valid.email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        invalid_input = True


def Username_Validation():
    global Username
    global invalid_input
    USERNAME_REGEX = re.compile(r"^[A-Za-z][A-Za-z0-9_]{7,29}$")
    if not USERNAME_REGEX.match(Username):
        print("Sorry your Email is not in the right format")
        Username = input("Please Enter your Email\n")
        return Username


def Password_Validation():
    global Password
    global invalid_input
    PASSWORD_REGEX = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
    if not PASSWORD_REGEX.fullmatch(Password):
        print("Sorry your Email is not in the right format")
        Password = input("Please Enter your Email\n")
        return Password


def input_details():  # Where the user will enter their details
    global Email
    global Username
    global Password

    Email = input("Please Enter your Email\n")
    Email_Validation()
    if invalid_input:
        input()
    Username = input("Please Enter your Username\n")
    Username_Validation()
    Password = input("Please Enter your Password\n")
    Password_Validation()


main_menu()
