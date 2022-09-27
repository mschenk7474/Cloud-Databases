"""
Created by Mason Schenk

Create: The class where we will br creating lists and points and sending them to the database.
"""

# all of the imports needed with the objects created for the connection to the database
import firebase_admin
import json
from firebase_admin import db
from list.user_auth import User_Authentication



class Create(User_Authentication):
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
        self.ref = db.reference("/Users")
        self.ref_point = db.reference("/Users")

    def type_to_create(self,r):
        """
        Asks the user what they would like to create.
        """

        # has the ref equal the new reference
        c = Create()
        self.ref = r
        self.ref_point = r

        print(self.ref)
        # opening prompt with choices for the user to choose from
        print("What type of data would you like to create? (Choose a number that corresponds to the options below)")
        print("1. An item of a list")
        print("2. A list")
        choice = int(input("> "))
        print()

        # handles case where the user wants to create an item for a list
        if choice == 1:
            c.item_input()
        
        # handles case where the user wants to create a list
        elif choice == 2:
            c.list_input()
        
        # handles the case where user inuts a number not supported
        else:
            print("Invalid choice, please try again.")
            print()
            c.type_to_create()

    def item_input(self):
        """
        Get's the list they would like the item to, and what the item would be.
        """
        c = Create()
        print("What list would you like to add the item to? ")
        list_choice = input("> ")

        if c.check_list(list_choice) == True:
            print(f"What item would you like to add to {list_choice}? ")
            item_choice = input("> ")
            
            if c.check_item(list_choice, item_choice) == False:
                c.create_item(list_choice, item_choice)
            else:
                print("That item is already present on the list, please try again.")
                print()
                c.item_input()
        else:
            print("The list name you entered is invalid, please try again.")
            print()
            c.item_input()

        pass

    def list_input(self):
        """
        Get's the list name to be added.
        """
        c = Create()
        print("What would you like to name your new list? ")
        list_name = input("> ")

        if c.check_list(list_name) == False:
            c.create_list(list_name)
        else:
            print("This list is already present, please try again")
            print()
            c.list_input()

    def create_list(self, lst):
        """
        Creates the list and adds it to the database. If the name already exisits,
        an error is thrown.
        """
        c = Create()
        user = User_Authentication()
        # print("We made it!")
        # sets a new user up in the database
            # self.creds = self.creds.child(f"{name}").child("Password")
            # self.creds.child("Password").set(password)
            # self.creds.set(name)
            # self.creds.set(password)
        self.ref = self.ref.child(f"{user.name}").child(lst)
        self.ref.set(f"{user.name}")
        # self.ref.set(lst)

        c.list_output()

    def create_item(self, list, item):
        """
        Creates the item on the specific list given by the user.
        """
        c = Create()
        user = User_Authentication()

        self.ref = self.ref.child(f"{user.name}").child(list).child(item)
        self.ref.set(item)

        c.item_output()

        # print("We made it!")
        

    def item_output(self):
        """
        A message saying the item has been created is displayed back to the user.
        """
        print("You have successfully added the item to the list!")
        print()

    def list_output(self):
        """
        A message saying the list has been created is displayed back to the user.
        """
        print("You have successfully added the list!")
        print()

    def check_list(self, lst):

        list_in_db = self.ref.get(self.ref_point)

        for x, y in enumerate(list_in_db):
            if lst in y:
                return True
            else:
                return False

    def check_item(self, lst, lst_item):
        list_in_db = self.ref.get(self.ref_point)

        for x, y in enumerate(list_in_db):
            if lst in y:
                if y[lst][lst_item] == lst_item:
                    return True
                else:
                    return False
            else:
                return False