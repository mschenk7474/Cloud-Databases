"""
Created by Mason Schenk

Delete: The class where we will be deleting points and lists.
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db



class Delete():
    """
    Delete will delete things permanetly from the databse. It will use the search class 
    capabilities to find the correct data to delete from the database.
    """

    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        self.ref = db.reference("/Users")

    def type_to_delete(self, r):
        """
        Asks the user what type of data they would like to delete.
        """
        # class instance declaration
        d = Delete()

        # has the ref equal the new reference
        self.ref = r
        
        # opening prompt with choices for the user to choose from
        print("What type of data would you like to delete? (Choose a number that corresponds to the options below)")
        print("1. An item of a list")
        print("2. A list")
        choice = int(input("> "))
        print()

        # handles case where the user wants to delete an item from a list
        if choice == 1:
            d.item_input()
        
        # handles case where the user wants to delete a list
        elif choice == 2:
            d.list_input()
        
        # handles the case where user inuts a number not supported
        else:
            print("Invalid choice, please try again.")
            d.type_to_delete()

    def item_input(self):
        """
        Asks the user to input the list and the item from the list they wish to be deleted.
        """
        pass
    
    def list_input(self):
        """
        Asks the user to input the list they wish to be deleted.
        """
        pass

    def item_delete(self):
        """
        Deletes the item from the list specified. Uses the search class to find the correct 
        item to delete.
        """
        pass

    def list_delete(self):
        """
        Deletes the list from the databse. Again, uses the search class to find the correct 
        item to delete.
        """
        pass

    def item_output(self):
        """
        Outputs a message that the item has been deleted.
        """
        pass

    def list_output(self):
        """
        Outputs a message saying that the list has been deleted.
        """
        pass