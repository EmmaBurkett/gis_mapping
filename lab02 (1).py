# 1. Name:
#      Emma Burkett
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is meant to take a username and a password from the 
#      user.  It then checks if their inputs match a username & password
#      pair in a user-selected json file.  It displays the result of the 
#      json search.
# 4. What was the hardest part? Be as specific as possible.
#      The initial assignment was mostly easy for me to complete, 
#      however, I wasn't sure how to error handle the keyword 'with.'  
#      I looked it up and found that most people use try/except.  
#      So, I understood how to do that part too. That's when I decided 
#      to jazz it up a bit and I added a list of available files for the 
#      user to select from.  
#
#      This required me to add a few imports and to use list 
#      comprehension.  I haven't used a lot of list comprehension so I 
#      enjoyed adding some if statements to it; I got the first half of 
#      the list comprehension online.  I also got to learn about
#      isinstance, which checks if a variable is a specified type and 
#      returns a boolean.  I also spent some time checking my error 
#      handling for any cracks and I wasn't able to break it! 
#
#      If I had to do this assignment again I would have check the 
#      length of my comment/code lines as I was writting them to make
#      sure that they follow the PEP 8 guidelines.
#
#      On lines 90-91 I made it so my print statment wasn't over the letter
#      limit and I missed moving my 'f' keyword to the right quotation.
#      On line 105 I should have just put '.' instead of my local 
#      directory name.
# 5. How long did it take for you to complete the assignment?
#      About four hours long.

import json
from os import listdir
from os.path import isfile, join

class Authentication:
    """Class Attributes:
        credentials: Dictornary for the json data.
        username: String for the user inputted username.
        password: String for the user inputted password.
        password_location: Integer that locates the correct password 
                           position.
        """

    def __init__(self):
        """This initializes the class attributes."""

        self.credentials = {}
        self.username = ""
        self.password = ""
        self.password_location = 0

    def main(self):
        """The main method runs the program."""

        # Get Json data.
        self.get_file()

        # Repeat for test cases.
        for i in range(7):

            # Get user_input.
            self.user_input()

            # Print result of authentication.
            print(self.authenticate(), "\n")

    def get_file(self):
        """The get_file method will prompt the user for a file name
        and call a function to read the file if it exists. 
        The function will recur until the file is succesfully read.
        """

        # Get file name from user.
        file_name = input("Which file do you want to open? ")

        # Error handle opening the file.
        try:
            
            # Get json as a list.
            self.credentials = self.read_file(file_name)
        except: 

            # Tell the user what went wrong.
            print("Oh! So, you didn't hear the question.",
            f"Unable to open file {file_name}.\n")

            # Display avalible files.
            self.directory_ls()

            # Recur the function.
            self.get_file()
        
    def directory_ls(self):
        """This method displays the available json files to be read.
        """

        # Uses list comprehension to create a list of json files in the 
        # current directory, lab02.
        json_list = [f for f in listdir('.') if (".json" in f and 
                                                self.json_check_formatting(f))]

        # Print list with correct formatting.
        print("Available Files: \n----------------", 
                *json_list, "", sep = "\n")

    def json_check_formatting(self, file_name):
        """This method tests the directories files for passwords and 
        usernames.  It also checks to make sure that they are lists, 
        which prevents errors in other functions.
        """

        # Call read_file method to get the json list.
        json_object = self.read_file(file_name)

        # Check the json list for the correct formatting and key words.
        if ("username" in json_object and 
            "password" in json_object and 
            isinstance(json_object["username"], list) and 
            isinstance(json_object["password"], list)):
            
            # Return a boolean.
            return True
        return False

    def user_input(self):
        """The user_input method gets the user's password, and username, 
        then it stores that into class attributes.
        """

        self.username = input("Please Enter Username: ")
        self.password = input("Please Enter Password: ")

    
    def read_file(self, file_name):
        """The read_file method will get the json file and 
        put it's information into a list and returns it.
        """

        # Read json file with error handling.
        with open(file_name, "r") as f:

            # Read json.
            file_text = f.read()

            # Store json data into class attribute. 
            credentials = json.loads(file_text)

            # Return a list.
            return credentials
        
    
    def authenticate(self):
        """This method calls other methods that check the users 
        username and password.  It returns a message to be displayed 
        to the user later.
        """

        # If the correct username and password is given then return 
        # corresponding message.
        if (self.authenticate_username()) and (self.authenticate_password()):
            return "Authenticated"
        else:
            return "Not authenticated"

    def authenticate_username(self):
        """This method checks if user input matches a valid username 
        in the json (now dictionary).  It returns a boolean.
        """

        # Enumerate through json dictionary while counting up from 
        # zero and storing that number.
        for self.password_location, name in enumerate(
                                                self.credentials["username"]):

            # If the user inputted username matches a json username 
            # return True.
            if name == self.username:
                return True
        return False

    def authenticate_password(self):
        """This method checks if user input matches the password 
        corrisponding to the inputted username in the json 
        (now dictionary).  It returns a boolean.
        """

        # If the user inputted password matches the username's password 
        # in the json dictionary then return True.
        if self.password == self.credentials["password"][
                                                    self.password_location]:
            return True
        else:
            return False

def main():
    """This function creates an object for the Authentication class 
       and calls the main method.
       """

    authenticate = Authentication()
    authenticate.main()

# This calls the function 'main()' above. 
if __name__ == "__main__":
    main()