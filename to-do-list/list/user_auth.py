"""
Created by Mason Schenk

User Authentication: Where the user inputs their credientials, and is 
directed to their correct part of the database.
"""
# all of the imports needed with the objects created for the connection to the database
from unicodedata import name
import firebase_admin
import json
from firebase_admin import db

class User_Authentication():
    """
    Within this class, we will have 3 main functions. They will be the intial prompt function
    that asks users if they have an account or not. If the user does have an account, they will be
    prompted using to input their name and password, and will be directed to the menu. If the user does not
    have a username and password, they will be directed to create both, and those will added to a new section of
    the database where the user may access that information any time they want with the correct username and 
    password inputted.
    """
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        # credentials to be gathered throughout the program. It is intially set for /Users
        self.creds = db.reference("/Users")
        self.name = " "

    def credentials_prompt(self):
        """
        Where we will ask if the user has an account or not. If
        not, they will be prompted to create an account and then to input their information.
        If they do already have an account, they will be directed to input their informaiton.
        """
        # class instance declaration
        ua = User_Authentication()

        # opening prompt and input
        print("Do you have an account (Y/N)?")
        choice = input("> ")
        print()

        # makes the user's choice upper just in case they enter a lowercase y or n
        choice = choice.upper()

        # directs to input if they already have an account
        if choice == "Y":
            ua.credentials_input()
        # directs them to create an account
        elif choice == "N":
            ua.credentials_create()
        
        # handles if the user inputs something that isn't accepted
        # also calls the prompt again to cycle through user input
        else:
            print("Invalid choice, please try again.")
            ua.credentials_prompt()
            

    def credentials_input(self):
        """
        Where the user will be asked to input their name and password. This function will return the name
        and password as the references to the database.
        """
        # class instance declaration
        ua = User_Authentication()

        # opening message to welcome users to the input menu
        print("ACCOUNT INPUT:")
        print()

        # name prompt
        print("Please enter the name of your account. (CASE SENSITIVE)")
        name = input("> ")
        print()

        # password prompt
        print("Please enter the password of your account. (CASE SENSITIVE)")
        password = input("> ")
        print()

        # makes sure the user name and password are correct and are in the database
        # if it is, in that order, it continues. If one is wrong, it returns an error.
        if ua.user_in_database(name, password) == True:

            # gets the correct reference, so that we can access the correct user's lists
            self.creds = self.creds.child("Users").child(f"{name}").child(f"{password}")

            # returns the ref to be used in the menu, but only off of the name since we want the
            # password to be it's own entity of the 
            self.creds = db.reference(f"/Users/{name}")
            self.name = name

        # error message with the recall to the prompt
        else:
            print("User is not in database, please try again.")
            ua.credentials_prompt()

    def credentials_create(self):
        """
        Where the user will be asked to create their name and password. Then the user will be 
        prompted to put their new name and password in by calling the input function
        """
        # class instance declaration
        ua = User_Authentication()

        # opening message to welcome the user to the account creation menu
        print("ACCOUNT CREATION:")
        print()

        # name prompt
        print("Please input the name you would like your account to be called. (CASE SENSITIVE)")
        name = input("> ")
        print()

        # password prompt
        print("Please input the password you would like the account under. (CASE SENSITIVE)")
        password = input("> ")
        print()

        # checks to make sure the information that the use inputs isn't in the database already.
        # if it isn't, it continues on with creation of the new account. If it is, error is returned.
        if ua.user_in_database(name, password) == False:

            # sets a new user up in the database
            self.creds = self.creds.child(f"{name}").child("Password")
            self.creds.child("Password").set(password)
            self.creds.set(name)
            self.creds.set(password)

            # message so the user knows what is going on
            print("Redirecting you to input the name and password you just created.")
            print()

            # call to the input function so the ref is made right
            ua.credentials_input()

        # error message with the recall to the prompt function
        else:
            print("User already exists, please try again")
            ua.credentials_prompt()


    def user_in_database(self, name, pswd):
        """
        This function will check to see if the user is in the database or not. The function
        will return a True if the user and password match another user and a false if it doesn't.
        """
        # gets all of the data from the user and sets it as the reference
        user_in_db = self.creds.get('/Users')
        #Check to see if name is in database using enumerate to go through all the data
        for x, y in enumerate(user_in_db):
            # if name is in tuple created
            if name in y:
                # if password is present as well
                if y[name]["Password"] == pswd:
                    return True
                # if password isn't present, return false
                else:
                    return False
            # if name isn't present, return falses
            else:
                return False
    def get_ref(self):
        return self.creds         