import tkinter as tk
import sqlite3

conn = sqlite3.connect('UserDatabase.db')

curs = conn.cursor()


class Login:
    def __init__(self, emailuser, Password):
        self.emailuser = emailuser
        self.password = Password

    def Verification(self):
        self.emailuser = input("Please enter your Email or Username \n")
        self.password = input("Please enter your password \n")
        verificationuser = f"SELECT Email from Records WHERE" \
                           f" Email='{self.emailuser}'" \
                           f" OR Username = '{self.emailuser}'" \
                           f" AND Password = '{self.password}';"
        curs.execute(verificationuser)
        if not curs.fetchone():  # An empty result evaluates to False.
            print("Login failed")
            self.Verification()
            return
        else:
            print("Welcome")


controller = Login("", "")
controller.Verification()
