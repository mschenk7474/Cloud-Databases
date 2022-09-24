"""
Created by Mason Schenk

Search: Where we wil be able to search for items in our 
databases, whether that be items of lists or lists themselves.
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db


class Search():
    """
    Search will be used by most other classes, but it's main goal is to search our database for
    data that will already be there. It will first ask what type of search we have. Then,
    it will ask what you are searching for, and then return the value to you to see it, if
    it is valid. If it is invalid, an error will pop up, and let us know the operation we
    tried to perform is incorrect
    """

    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        self.ref = db.reference("/Users")

    def type_to_search(self, r):
        """
        Where we will narrow down what type of search we will be doing, and direct the efforts
        in the correct direction.
        """
        # class instance declaration
        s = Search()

        # has the ref equal the new reference
        self.ref = r

        # opening prompt with choices for the user to choose from
        print("What type of data would you like to search for? (Choose a number that corresponds to the options below)")
        print("1. An item of a list")
        print("2. A list")
        choice = int(input("> "))
        print()

        # handles case where the user wants to search for an item from a list
        if choice == 1:
            s.item_input()
        
        # handles case where the user wants to search for a list
        elif choice == 2:
            s.list_input()
        
        # handles the case where user inuts a number not supported
        else:
            print("Invalid choice, please try again.")
            s.type_to_search()
    
    def item_input(self):
        """
        Gets the item the user is looking for.
        """
        pass

    def list_input(self):
        """
        Gets the list the user is looking for.
        """
        pass

    def item_search(self):
        """
        Searches the database for the item, which will be on a list, and returns it.
        If item is not on list or in database, returns error.
        """
        pass

    def list_search(self):
        """
        Searches the database for the list and returns it.
        If list not present in database, returns error.
        """
        pass
    
    def item_output(self):
        """
        Outputs the list the item is on.
        """
        pass

    def list_output(self):
        """
        Outputs the list the user was search for.
        """
        pass