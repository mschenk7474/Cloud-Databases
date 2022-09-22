"""
Create: The class where we will br creating lists and points and sending them to the database.
"""

# class declaration
from list.search import Search

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
        pass

    def type_to_create(self):
        """
        Asks the user what they would like to create.
        """
        pass

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