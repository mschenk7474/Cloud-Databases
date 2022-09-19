"""
User Authentication: Where the user inputs their credientials, and is 
directed to their correct part of the database.
"""

class User_Authentication():
    """
    Within this class, we will have 3 main functions. They will be the intial prompt function
    that asks users if they have an account or not. If the user does have an account, they will be
    prompted using to input their name and password, and will be directed to the menu. If the user does not
    have a username and password, they will be directed to create both, and those will added to a new section of
    the database where the user may access that information any time they want with the correct username and 
    password inputted.
    """
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        pass

    def credentials_prompt(self):
        """
        Where we will ask if the user has an account or not. If
        not, they will be prompted to create an account and then to input their information.
        If they do already have an account, they will be directed to input their informaiton.
        """
        pass

    def credentials_input(self):
        """
        Where the user will be asked to input their name and password.
        """
        pass

    def credentials_create(self):
        """
        Where the user will be asked to create their name and password.
        """
        pass