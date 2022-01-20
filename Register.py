from email_validator import validate_email, EmailNotValidError
import tkinter as tk
import re
import sqlite3

conn = sqlite3.connect('UserDatabase.db')

curs = conn.cursor()


class Credentials:
    def __init__(self, Email, Username, Password, Failcheck, Fail):
        self.email = Email
        self.username = Username
        self.password = Password
        self.failcheck = Failcheck
        self.fail = Fail

    def Email_Validation(self):  # Validates that the fields the user enters are correct
        try:
            # Validate.
            valid = validate_email(self.email)

            # Update with the normalized form.
            email = valid.email
            self.fail = 0
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            self.failcheck = True
            self.fail = 1

    def Username_Validation(self):
        USERNAME_REGEX = re.compile(r"^[A-Za-z][A-Za-z0-9_]{7,29}$")
        if not USERNAME_REGEX.match(self.username):
            print("Sorry your Username is not in the right format")
            self.failcheck = True
            self.fail = 1
        else:
            self.fail = 0

    def Password_Validation(self):
        PASSWORD_REGEX = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
        if not PASSWORD_REGEX.fullmatch(self.password):
            print("Sorry your Password is not in the right format")
            self.failcheck = True
            self.fail = 1
        else:
            self.fail = 0

    def email_database(self):
        self.fail = 0
        self.failcheck = False
        self.email = input("Please Enter your Email\n")
        self.Email_Validation()
        if self.failcheck:
            while self.fail == 1:
                self.email = input("Please Enter your Email\n")
                self.Email_Validation()
        self.failcheck = False
        self.username = input("Please Enter your Username\n")
        self.Username_Validation()
        if self.failcheck:
            while self.fail == 1:
                self.username = input("Please Enter your Username\n")
                self.Username_Validation()
        self.failcheck = False
        self.password = input("Please Enter your Password\n")
        self.Password_Validation()
        if self.failcheck:
            while self.fail == 1:
                self.password = input("Please Enter your Password\n")
                self.Password_Validation()
        print(self.email, self.username, self.password)


register = Credentials("", "", "", False, 0)
register.email_database()