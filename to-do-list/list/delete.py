"""
Created by Mason Schenk

Delete: The class where we will be deleting points and lists.
"""

# class declaration
from list.search import Search

class Delete():
    """
    Delete will delete things permanetly from the databse. It will use the search class 
    capabilities to find the correct data to delete from the database.
    """

    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        pass

    def type_to_delete(self):
        """
        Asks the user what type of data they would like to delete.
        """
        pass

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