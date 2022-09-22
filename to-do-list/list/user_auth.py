"""
User Authentication: Where the user inputs their credientials, and is 
directed to their correct part of the database.
"""
# all of the imports needed with the objects created for the connection to the database
import sys
import firebase_admin
import json
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('/Users/masonschenk/Documents/BYUI/BYUI Fall 2022/Applied Programming/Cloud Databases/CD Code/fir-cd-9586a-firebase-adminsdk-eevq2-f56bb1536d.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://fir-cd-9586a-default-rtdb.firebaseio.com'
	})

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

    def credentials_prompt():
        """
        Where we will ask if the user has an account or not. If
        not, they will be prompted to create an account and then to input their information.
        If they do already have an account, they will be directed to input their informaiton.
        """
        # opening prompt and input
        print("Do you have an account (Y/N)?")
        choice = input("> ")
        print()

        # makes the user's choice upper just in case they enter a lowercase y or n
        choice.upper()

        # directs to input if they already have an account
        if choice == "Y":
            User_Authentication.credentials_input()
        # directs them to create an account
        elif choice == "N":
            User_Authentication.credentials_create()
        
        # handles if the user inputs something that isn't accepted
        else:
            print("Invalid choice, please try again.")
            # uses sys.exit to exit the program so the menu isn't ran
            sys.exit()
            

    def credentials_input():
        """
        Where the user will be asked to input their name and password. This function will return the name
        and password as the references to the database.
        """
        # opening message to welcome users to the input menu
        print("ACCOUNT INPUT:")
        print()

        # name prompt
        print("Please enter the name of your account.")
        name = input("> ")
        print()

        # password prompt
        print("Please enter the password of your account.")
        password = input("> ")
        print()

        # ERROR, NEEDS TO SEARCH FOR THE ACCOUNT AND IF NOT THERE, GIVE ERROR MESSAGE (implement after doing search)
        
        # gets the correct reference, so that we can access the correct user's lists
        ref = db.reference("/Users")
        ref = ref.child("Users").child(f"{name}").child(f"{password}")

        # returns the ref to be used in the menu
        return ref

    def credentials_create():
        """
        Where the user will be asked to create their name and password. Then the user will be 
        prompted to put their new name and password in by calling the input function
        """
        # opening message to welcome the user to the account creation menu
        print("ACCOUNT CREATION:")
        print()

        # name prompt
        print("Please input the name you would like your account to be called.")
        name = input("> ")
        print()

        # password prompt
        print("Please input the password you would like the account under.")
        password = input("> ")
        print()

        # ERROR, NEEDS TO SEARCH FOR THE ACCOUNT AND IF NOT THERE, GIVE ERROR MESSAGE (implement after doing search)

        # sets a new user up in the database
        ref = db.reference("/Users")
        ref = ref.child(f"{name}").child(f"{password}")
        ref.set(name)
        ref.set(password)

        # message so the user knows what is going on
        print("Redirecting you to input the name and password you just created.")
        print()

        # call to the input function so the ref is made right
        User_Authentication.credentials_input()