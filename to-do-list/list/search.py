"""
Search: Where we wil be able to search for items in our 
databases, whether that be items of lists or lists themselves.
"""

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
        pass

    def type_to_search(self):
        """
        Where we will narrow down what type of search we will be doing, and direct the efforts
        in the correct direction.
        """
        pass
    
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