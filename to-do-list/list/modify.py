"""
Created by Mason Schenk

Modify: Where we will be modifying certain points and lists.
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db



class Modify():
    """
    Modify is going to be used when the user wants to update an item or list they have made.
    Modify will use search to find the items and lists to update, and will update the items
    and lists that are valid, due to that class' error checking.
    """
    
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        self.ref = db.reference("/Users")

    def type_to_modify(self, r):
        """
        Asks the user whether they would like to modify a list or an item of a list.
        """
        # class instance declaration
        m = Modify()

        # has the ref equal the new reference
        self.ref = r

        # opening prompt with choices for the user to choose from
        print("What type of data would you like to modify? (Choose a number that corresponds to the options below)")
        print("1. An item of a list")
        print("2. A list")
        choice = int(input("> "))
        print()

        # handles case where the user wants to modify an item for a list
        if choice == 1:
            m.item_input()
        
        # handles case where the user wants to modify a list
        elif choice == 2:
            m.list_input()
        
        # handles the case where user inuts a number not supported
        else:
            print("Invalid choice, please try again.")
            m.type_to_modify()

    def item_input(self):
        """
        Get's the list and item that the user wants to modify.
        """
        pass
    
    def list_input(self):
        """
        Get's the list the user wants to modify.
        """
        pass

    def modify_item(self):
        """
        Modifies the certain item from the specified list the user wanted. This
        will use the search class to find the correct list and item, and then the
        method will update the database of the modified item.
        """
        pass

    def modify_list(self):
        """
        Modifies the list the user wanted and updates the database with the new 
        information.
        """
        pass

    def output_item(self):
        """
        Outputs a message to the user advising them the change has been made!
        """
        pass

    def output_list(self):
        """
        Outputs a message to the user advising them the change has been made!
        """
        pass