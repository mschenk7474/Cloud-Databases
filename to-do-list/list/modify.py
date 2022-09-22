"""
Modify: Where we will be modifying certain points and lists.
"""
# class declarations
from list.search import Search

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
        pass

    def type_to_modify(self):
        """
        Asks the user whether they would like to modify a list or an item of a list.
        """
        pass

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