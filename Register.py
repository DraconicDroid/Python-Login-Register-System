from email_validator import validate_email, EmailNotValidError
import tkinter as tk
import re


class Credentials:
    def __init__(self, Email, Username, Password):
        self.email = Email
        self.username = Username
        self.password = Password

    def Email_Validation(self, Email):  # Validates that the fields the user enters are correct
        try:
            # Validate.
            valid = validate_email(Email)

            # Update with the normalized form.
            email = valid.email
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            self.input_Email(Email)

    def Username_Validation(self, Username):
        USERNAME_REGEX = re.compile(r"^[A-Za-z][A-Za-z0-9_]{7,29}$")
        if not USERNAME_REGEX.match(Username):
            print("Sorry your Username is not in the right format")
            self.input_Username(Username)

    def Password_Validation(self, Password):
        PASSWORD_REGEX = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
        if not PASSWORD_REGEX.fullmatch(Password):
            print("Sorry your Password is not in the right format")
            self.input_Password(Password)

    def input_Email(self, Email):  # Where the user will enter their details
        Email = input("Please Enter your Email\n")
        self.Email_Validation(Email)
        return Email

    def input_Username(self, Username):  # Where the user will enter their details
        Username = input("Please Enter your Username\n")
        self.Username_Validation(Username)
        return Username

    def input_Password(self, Password):  # Where the user will enter their details
        Password = input("Please Enter your Password\n")
        self.Password_Validation(Password)
        return Password
        self.just_checking(Email, Password, Username)

    def just_checking(self, Email, Password, Username):
        Email = self.input_Email()
        Password = self.input_Email()
        Username = self.input_Email()
        print(Email, Password, Username)


register = Credentials("", "", "")
register.input_Email("")
register.input_Username("")
register.input_Password("")
