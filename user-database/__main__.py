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
from user_db.user import User
def main():
    """
    This is the main function, where everything is ran from. Only classes needed here is the user class. 
    We get the intial credentials prompt, and then call the menu within the user class to intialize
    the program.
    """
    # class instance declarations
    user = User()

    # calls to authenticate the user and gets reference to user throughout the program
    user.credentials_prompt()

    #calls the menu 
    user.menu()
    
    

# runs main
if __name__ == "__main__":
    main()