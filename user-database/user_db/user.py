"""
Created by Mason Schenk

User: Where the user inputs their credientials, chooses what to in a menu, and closes the program
whenever they would like.
"""
# all of the imports needed 
from firebase_admin import db

class User():
    """
    This class has a couple main functions. It holds the ways the user will input, create, modify,
    show, and delete credentials. On each of these main functions, there will be checks that go 
    through the database and make sure there aren't duplicates where they shouldn't be. This is all
    done through a UI of a menu, with options to do each of the tasks explained above.
    """
    def __init__(self):
        """
        Where we will intialize all the public variables to be used throughout the class.
        """
        # credentials to be gathered throughout the program. It is intially set for /Users
        self.creds = db.reference("/Users")
        self.name = " "

    def credentials_prompt(self):
        """
        Where we will ask if the user has an account or not. If
        not, they will be prompted to create an account and then to input their information.
        If they do already have an account, they will be directed to input their informaiton.
        """
        # class instance declaration
        ua = User()

        # opening prompt and input
        print("Do you have an account (Y/N)?")
        choice = input("> ")
        print()

        # makes the user's choice upper just in case they enter a lowercase y or n
        choice = choice.upper()

        # directs to input if they already have an account
        if choice == "Y":
            ua.credentials_input()
        # directs them to create an account
        elif choice == "N":
            ua.credentials_create()
        
        # handles if the user inputs something that isn't accepted
        # also calls the prompt again to cycle through user input
        else:
            print("Invalid choice, please try again.")
            ua.credentials_prompt()
            

    def credentials_input(self):
        """
        Where the user will be asked to input their name and password. This function will return the name
        and password as the references to the database.
        """
        # class instance declaration
        ua = User()

        # opening message to welcome users to the input menu
        print("ACCOUNT INPUT:")
        print()

        # name prompt
        print("Please enter the name of your account. (CASE SENSITIVE)")
        name = input("> ")
        print()

        # password prompt
        print("Please enter the password of your account. (CASE SENSITIVE)")
        password = input("> ")
        print()

        # makes sure the user name and password are correct and are in the database
        # if it is, in that order, it continues. If one is wrong, it returns an error.
        if ua.user_in_database(name, password) == True:

            # gets the correct reference, so that we can access the correct user's lists
            self.creds = self.creds.child("Users").child(f"{name}").child(f"{password}")

            # returns the ref to be used in the menu, but only off of the name since we want the
            # password to be it's own entity of the 
            self.creds = db.reference(f"/Users/{name}")
            self.name = name

        # error message with the recall to the prompt
        else:
            print("User is not in database, please try again.")
            ua.credentials_prompt()

    def credentials_create(self):
        """
        Where the user will be asked to create their name and password. Then the user will be 
        prompted to put their new name and password in by calling the input function
        """
        # class instance declaration
        ua = User()

        # opening message to welcome the user to the account creation menu
        print("ACCOUNT CREATION:")
        print()

        # name prompt
        print("Please input the name you would like your account to be called. (CASE SENSITIVE)")
        name = input("> ")
        print()

        # password prompt
        print("Please input the password you would like the account under. (CASE SENSITIVE)")
        password = input("> ")
        print()

        # checks to make sure the information that the use inputs isn't in the database already.
        # if it isn't, it continues on with creation of the new account. If it is, error is returned.
        if ua.user_in_database(name, password) == False:

            # sets a new user up in the database
            self.creds = self.creds.child(f"{name}").child("Password")
            self.creds.child("Password").set(password)
            self.creds.set(name)
            self.creds.set(password)

            # message so the user knows what is going on
            print("Redirecting you to input the name and password you just created.")
            print()

            # call to the input function so the ref is made right
            ua.credentials_input()

        # error message with the recall to the prompt function
        else:
            print("User already exists, please try again")
            ua.credentials_prompt()


    def user_in_database(self, name, pswd):
        """
        This function will check to see if the user is in the database or not. The function
        will return a True if the user and password match another user and a false if it doesn't.
        """
        # gets all of the data from the user and sets it as the reference
        user_in_db = self.creds.get('/Users')
        #Check to see if name is in database using enumerate to go through all the data
        for x, y in enumerate(user_in_db):
            # if name is in tuple created
            if name in y:
                # if password is present as well
                if y[name]["Password"] == pswd:
                    return True
                # if password isn't present, return false
                else:
                    return False
            # if name isn't present, return falses
            else:
                return False      
    
    def credentials_show(self):
        """
        This function shows the user credentials of an account that they can enter.
        It gets the name from the user, checks to make sure it is in the database, 
        and displays the account information.
        """
        # class intialization
        ua = User()

        # opening message
        print("ACCOUNT CREDENTIALS")
        print()

        # asks for the account name to be shown back to the user
        print("What account details would you like to see? ")
        account_to_find = input("> ")
        print()

        # sets data so enumerate can go through the database correctly
        data = self.creds.get("/Users")

        # for loop that goes through the database
        for x,y in enumerate(data):
            # returns true if the account name the user inputted is in the database
            if account_to_find in y:
                # sets password to be displayed back to the user
                pswd = y[account_to_find]["Password"]

                # display messgae of the account information
                print(f"The name of the account is {account_to_find} and the password is {pswd}.")
                print()
                return

            # if the user isn't found, errror message with it looping back to input correct credentials
            else:
                print("User is not found, please try again.")
                print()
                ua.credentials_show()
                return

        # call of the menu because we aren't done until the user quits out of the main menu
        ua.menu()

    def credentials_modify(self):
        """
        Where credentials are modified. The user is asked whether they want to change
        the name or password on the account, and each is done with all of the error
        checking needed to perform the purpose of the function.
        """
        # class intialization
        ua = User()

        # declaration of the variables to be used later on in the project
        # self.creds for getting specific values from the database
        # data for getting all the data from the database
        self.creds = db.reference("/Users")
        data = self.creds.get("/Users")

        # opening message
        print("ACCOUNT MODIFICATION")
        print()

        # asks the user whether they would like to modify name or password
        print("What account details would you like to modify? ")
        print("1. Name")
        print("2. Password")
        account_to_modify_type = int(input("> "))
        print()

        # name option
        if account_to_modify_type == 1:
            # asks the user what name they would like to change
            print("What name would you like to change? ")
            name_b4 = input("> ")
            print()
            
            # for loop to go through all the data
            for x,y in enumerate(data):
                # checks to make sure the user is in the data
                if name_b4 in y:
                    # asks the user what they would like to change the user to
                    print(f"what would you like to change {name_b4} to? ")
                    name_after = input("> ")
                    print()
                    # checks to make sure the new user is not in the database already
                    if name_after not in y:
                        # declares the before password's value as a temp value
                        name_b4_password = y[name_b4]["Password"]

                        # deletes the old name and its contents
                        delete = self.creds.child(name_b4)
                        delete.delete()

                        # sets the new name and adds the child to it
                        self.creds.child(name_after)
                        self.creds.child(name_after).child("Password").set(name_b4_password)

                        # outputs success message when the name has been modified
                        print("User has been successfully modified!")
                        print()
                        return
                    # if the new user is already present in the database, an error message is
                    # printed and the user is directed back to the start of the function to input
                    # the correct crendtials
                    else:
                        print("User is already in database, please try again.")
                        print()
                        ua.credentials_modify()
                        return
                # if the user is not found in the data, an error messaged is printed and the user
                # is directed back to the start of the function to input correct credentials
                else:
                    print("User not found, please try again.")
                    print()
                    ua.credentials_modify()
                    return
            # call of the menu because we aren't done until the user quits out of the main menu
            ua.menu()

        # password option
        elif account_to_modify_type == 2:
            # for loop to go through the entire data set
            for x, y in enumerate(data):
                # gets the name the password is under
                print("What name is the password under? ")
                name_of_user = input("> ")
                print()
                # checks to make sure the user is in the database
                if name_of_user in y:
                    # gets the current password
                    print("What is the current password? ")
                    curr_pswd = input("> ")
                    print()
                    # checks to make sure the password for the user is correct
                    if y[name_of_user]["Password"] == curr_pswd:
                        # gets what the user wants to change the password to
                        print("What woud you like to change the password to? ")
                        new_pswd = input("> ")
                        print()

                        # sets the new password in place of the old one
                        self.creds.child(name_of_user).child("Password").set(new_pswd)
                        
                        # success message to be displayed once password is modified
                        print("Password has been successfully modified!")
                        print()
                        return
                    # if the password the user inputs is incorrect, an error message is 
                    # displayed, and the user is directed back to the start of the function
                    # to input the correct credentials
                    else:
                        print("That is not the correct password, please try again.")
                        print()
                        ua.credentials_modify()
                        return
                # if the user is not present, an error message is displayed, and the user is
                # directed back to the start of the function
                else:
                    print("User is not present in database, please try again.")
                    print()
                    ua.credentials_modify()
                    return
            # call of the menu because we aren't done until the user quits out of the main menu
            ua.menu()
        else:
            print("Not a valid choice, please try again.")
            print()
            ua.credentials_modify()

    def credentials_delete(self):
        """
        This function deletes a user from the database. It gets the user, makes sure
        that the user is in the database, and then deletes it and its data from the
        server.
        """
        # class intialization
        ua = User()

        # opening message
        print("ACCOUNT DELETION: ")
        print()

        # asks the user to input what they would like to delete
        print("What user would you like to delete? ")
        user_to_delete = input("> ")
        print()

        # declares self.creds to be used later, and declares data to be used by enumerate
        self.creds = db.reference("/Users")
        data = self.creds.get("/Users")

        # for loop that goes through the database
        for x, y in enumerate(data):
            # checks to make sure the user is in the database
            if user_to_delete in y:
                # declares delete_user as the name in the database wanting to be deleted by the user
                delete_user = self.creds.child(user_to_delete)

                # utilizes the delete command from firebase to delete the user from the database
                delete_user.delete()

                # display message of the account being successfully deleted
                print("User has been deleted!")
                print()
                return 
            
            # if the user isn't in the database, an error message is printed, and the user is 
            # directed back to input correct credentials
            else:
                print("User does not exist, please try again.")
                print()
                ua.credentials_delete()
                return
        # call of the menu because we aren't done until the user quits out of the main menu
        ua.menu()
                

    def menu(self):
        """
        Where the user chooses what option they would like, and the corresponding calls to the 
        function go as the user would like.
        """
        # intializes the choice variable and the class instance
        ua = User()
        done = False
        
        # opening message
        print("Welcome to the User Menu!")
        print()

        # main menu with all the different options
        while done != True:
            print("Pick from the options below:")
            print("1. Create User and Password")
            print("2. Show User and Password")
            print("3. Modify User and Password")
            print("4. Delete User and password")
            print("5. Quit")
            choice = int(input("Enter number here > "))
            print()

            # actual choices using if's
            # create choice
            if choice == 1:
                # only has to call this one function 
                ua.credentials_create()
            
            # search choice
            elif choice == 2:
                # only has to call this one function 
                ua.credentials_show()

            # modify choice
            elif choice == 3:
                # only has to call this one function 
                ua.credentials_modify()
            
            # delete choice
            elif choice == 4:
                # only has to call this one function 
                ua.credentials_delete()
            
            # quit choice
            elif choice == 5:
                # fun little message to output
                print("Session Terminated")

                # while loop counter set to true to break loop
                done = True
            
            #handles when the user doesn't put in a number 1-5
            else:
                print("Invalid choice, please try again.")