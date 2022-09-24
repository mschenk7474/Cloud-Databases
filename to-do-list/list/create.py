"""
Created by Mason Schenk

Create: The class where we will br creating lists and points and sending them to the database.
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db



class Create():
    """
    Create is for when the user wants to create either a new item or list. This is the
    primary way the user will add data to the database, for them to pull from whenever they
    may feel like it. Create will use the search class here to error check and make sure 
    we are not having duplicate items or lists within our database.
    """
    
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        self.ref = db.reference("/Users")

    def type_to_create(self,r):
        """
        Asks the user what they would like to create.
        """
        # class instance declaration
        c = Create()

        # has the ref equal the new reference
        self.ref = r

        # opening prompt with choices for the user to choose from
        print("What type of data would you like to create? (Choose a number that corresponds to the options below)")
        print("1. An item of a list")
        print("2. A list")
        choice = int(input("> "))
        print()

        # handles case where the user wants to create an item for a list
        if choice == 1:
            c.item_input()
        
        # handles case where the user wants to create a list
        elif choice == 2:
            c.list_input()
        
        # handles the case where user inuts a number not supported
        else:
            print("Invalid choice, please try again.")
            c.type_to_create()

    def item_input(self):
        """
        Get's the list they would like the item to, and what the item would be.
        """
        pass

    def list_input(self):
        """
        Get's the list name to be added.
        """
        pass

    def create_list(self):
        """
        Creates the list and adds it to the database. If the name already exisits,
        an error is thrown.
        """
        pass

    def create_item(self):
        """
        Creates the item on the specific list given by the user. If the item is
        already on the list, an error is thrown.
        """
        pass

    def item_output(self):
        """
        A message saying the item has been created is displayed back to the user.
        """
        pass

    def list_output(self):
        """
        A message saying the list has been created is displayed back to the user.
        """
        pass