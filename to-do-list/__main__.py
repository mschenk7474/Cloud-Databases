"""
Main file: where everthing is compiled and ran from
"""

# class calls
from list.user_auth import User_Authentication
from list.menu import Menu

def main():
    """
    This is the main function, where everything is ran from. Only classes needed here are the menu and 
    user authentication classes. We need to get the UA from the user, pass that as the reference in the 
    database to the menu, and then use that when pulling up the user's past entries into the database.
    """

    # calls to authenticate the user (will pass the reference for the menu to use later on in the functionality)
    credentials = User_Authentication.credentials_prompt()

    #calls the menu (will get passed the credentials, nothing in it right now)
    Menu.menu(credentials)

# runs main
if __name__ == "__main__":
    main()