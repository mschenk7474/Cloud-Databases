"""
Created by Mason Schenk

Menu: Where we will have all the options come from. Will have a 
menu with the options that coorelates to the specific classes needed.
"""

# class calls
from list.create import Create
from list.delete import Delete
from list.modify import Modify
from list.search import Search

class Menu():
    """
    Menu holds the one function it needs, the menu. All it handles is the generation of the menu
    and the call of classes. It handles one error cases, but the classes hold up most of the heavy
    lifting, making the readability here in the menu a lot easier on the eyes.
    """
    
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """

    def menu(self, ref):

        # ref is equal to /users/whatever_name_was_inputted
        
        # intializes the choice variable
        done = False
        
        # opening message
        print("Welcome to the To-Do List Menu!")
        print()

        # main menu with all the different options
        while done != True:
            print("Pick from the options below:")
            print("1. Create")
            print("2. Search")
            print("3. Modify")
            print("4. Delete")
            print("5. Quit")
            choice = int(input("Enter number here > "))
            print()

            # actual choices using if's
            # create choice
            if choice == 1:
                # only has to call this one function with the class instance, everything else is handled within the class
                c = Create()
                c.type_to_create(ref)
            
            # search choice
            elif choice == 2:
                # only has to call this one function with the class instance, everything else is handled within the class
                s = Search()
                s.type_to_search(ref)

            # modify choice
            elif choice == 3:
                # only has to call this one function with the class instance, everything else is handled within the class
                m = Modify()
                m.type_to_modify(ref)
            
            # delete choice
            elif choice == 4:
                # only has to call this one function with the class instance, everything else is handled within the class
                d = Delete()
                d.type_to_delete(ref)
            
            # quit choice
            elif choice == 5:
                # fun little message to output
                print("Session Terminated")

                # while loop counter set to true to break loop
                done = True
            
            #handles when the user doesn't put in a number 1-5
            else:
                print("Invalid choice, please try again.")