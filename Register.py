from email_validator import validate_email, EmailNotValidError
import tkinter as tk
import re
import sqlite3

conn = sqlite3.connect('UserDatabase.db')  # This connects the database to python file

curs = conn.cursor()  # This allows me to interact with the database


class Register:
    def __init__(self, Email, Username, Password, Failcheck, Fail, Emailyes):
        # initializes the class with the parameters I specified below
        self.email = Email
        self.username = Username
        self.password = Password
        self.failcheck = Failcheck
        self.fail = Fail
        self.emailyes = Emailyes

    def Email_Validation(self):  # Validates that the email the user entered is correct
        try:
            # Validates the email.
            valid = validate_email(self.email)

            self.fail = 0
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            self.failcheck = True  # this occurs when the email is incorrect and enables a loop that is explained below
            self.fail = 1

    def Username_Validation(self):
        USERNAME_REGEX = re.compile(r"^[A-Za-z][A-Za-z0-9_]{7,29}$")
        # Username regex (must be 8 character but less than 28 and cannot include special characters)
        if not USERNAME_REGEX.match(self.username):
            print("Sorry your Username is not in the right format")
            self.failcheck = True
            self.fail = 1
        else:
            self.fail = 0

    def Password_Validation(self):
        PASSWORD_REGEX = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
        # Password regex (must be 8 characters or more and cannot include special characters)
        if not PASSWORD_REGEX.fullmatch(self.password):
            print("Sorry your Password is not in the right format")
            print("Your password must be 8 characters or more and cannot include special characters")
            self.failcheck = True
            self.fail = 1
        else:
            self.fail = 0

    def input_Email(self):
        self.fail = 0
        self.failcheck = False
        emailQ = input("Would you like to register an email\n")
        if emailQ in ["Yes", "yes", "Y", "y"]:
            self.emailyes = True
            self.email = input("Please Enter your Email\n")
            self.Email_Validation()
            if self.failcheck:
                while self.fail == 1:
                    self.email = input("Please Enter your Email\n")
                    self.Email_Validation()
        elif emailQ in ["No", "no", "N", "n"]:
            self.emailyes = False
            print("Your email won't be registered")
        else:
            print("Invalid input: you must enter yes or no")
            self.input_Email()
            return
        self.input_Username()

    def input_Username(self):
        self.failcheck = False
        print("")
        print("")
        print("Your Username must be 8 characters but less than 29 and cannot include special characters")
        self.username = input("Please Enter your Username\n")
        self.Username_Validation()
        if self.failcheck:
            while self.fail == 1:
                print("Your Username must be 8 characters but less than 29 and cannot include special characters")
                self.username = input("Please Enter your Username\n")
                self.Username_Validation()
        self.input_Password()

    def input_Password(self):
        self.failcheck = False
        print("")
        print("")
        print("Your password must be 8 characters or more and cannot include special characters")
        self.password = input("Please Enter your Password\n")
        self.Password_Validation()
        if self.failcheck:
            while self.fail == 1:
                print("Your password must be 8 characters or more and cannot include special characters")
                self.password = input("Please Enter your Password\n")
                self.Password_Validation()
        self.Credentials_database()

    def Credentials_database(self):
        print(self.email, self.username, self.password)
        if self.emailyes:
            curs.execute("INSERT INTO Records (Email, Username, Password) VALUES (?, ?, ?)",
                         (self.email, self.username, self.password))
            conn.commit()
            conn.close()
        if not self.emailyes:
            curs.execute("INSERT INTO Records (Username, Password) VALUES (?, ?)",
                         (self.username, self.password))
            conn.commit()
            conn.close()


controller = Register("", "", "", False, 0, True)
controller.input_Email()
