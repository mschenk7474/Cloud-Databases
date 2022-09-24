"""
Created by Mason Schenk

Main file: where everthing is compiled and ran from
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('/Users/masonschenk/Documents/BYUI/BYUI Fall 2022/Applied Programming/Cloud Databases/CD Code/fir-cd-9586a-firebase-adminsdk-eevq2-f56bb1536d.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://fir-cd-9586a-default-rtdb.firebaseio.com'
	})

# class calls
from list.user_auth import User_Authentication
from list.menu import Menu
def main():
    """
    This is the main function, where everything is ran from. Only classes needed here are the menu and 
    user authentication classes. We need to get the UA from the user, pass that as the reference in the 
    database to the menu, and then use that when pulling up the user's past entries into the database.
    """
    # class instance declarations
    user = User_Authentication()
    main_menu = Menu()

    # calls to authenticate the user and gets reference to user throughout the program
    user.credentials_prompt()
    ref = user.get_ref()
    
    #calls the menu (will get passed the credentials, nothing in it right now)
    main_menu.menu(ref)

# runs main
if __name__ == "__main__":
    main()