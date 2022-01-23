'''
Welcome to the program section of the Python Crash Course. This program is going
to bring together some of the examples from example.py, and hopefully help you
write Python too!

The purpose of this program is to accept a JSON file name as an argument in the
command line, then deserialize that file into a readable object. After that,
the program will let you edit some of the details of that object then
reserialize back to the JSON file.
'''

# We're going to use an enum for menu pages so that it's easier to keep track of
# what page we're on.
from enum import Enum
# We're also going to need to get a system file path, so we can use pathlib.
from pathlib import Path
# And we're going to need to parse arguments given via the command line.
import argparse
# And the most important element, the JSON library to deserialize and
# reserialize the Person's information.
import json


class Person:
    # We're going to provide the given filename to the initializer so the class
    # can store that information.
    def __init__(self, filename: str):
        # This docstring has some info about its arguments because "filename"
        # isn't descriptive enough to know what it is.
        """
        Initialize the Person class.

        Arguments:
        filename -- the filename to load the Person instance from
        """
        self.first_name = ""
        self.middle_initial = ''
        self.last_name = ""
        self.age = -1
        self.address = ""
        self.married = False
        self.spouse = {}
        self.children = []
        # This uses Path from pathlib to combine the filename and create an
        # object. The path will look like "./john_smith.json", while the object
        # will have file-specific functions.
        self.file = Path(".") / filename

    def load(self):
        """Load the Person from the provided file."""
        # This line ensures that file exists and is not a directory or other
        # invalid item.
        if not self.file.is_file():
            print("Invalid file.")
            return

        # Open the file in read mode. "with" closes the file at the end of the 
        # scope (the "with" block). Without it, we would have to manually close
        # the file with file.close().
        with open(self.file, "r") as file:
            # __dict__ is a reference to all the member variables of this class
            # as a dictionary. We use the update() function to take any values
            # in the JSON file and attach them to their corresponding variables.
            self.__dict__.update(json.load(file))

    def save(self):
        """Save the Person to the provided file."""
        # Ensure that the file hasn't changed since it was loaded. We're not
        # using file.is_file() because we want to overwrite it even if it
        # exists.
        if self.file.is_dir() or self.file.is_symlink():
            raise ValueError("File path should point to a valid file. "
                             f"Given: {self.file}")

        # self.file isn't writeable to JSON; it's a special object that is not
        # serialized. Therefore, we have to make a copy of all the member
        # variables in a new dictionary and then delete the offending variable.
        to_write = self.__dict__.copy()
        del to_write["file"]

        # Then we can open the file with write access and dump the new JSON
        # into it.
        with open(self.file, "w+") as file:
            json.dump(to_write, file, indent=4, sort_keys=False)

    def is_valid(self):
        """Check if the Person instance is valid."""
        if self.first_name == "" or self.age == -1:
           return False

        return True

    def get_name(self):
        """Get the formatted name of the Person."""
        # Ooo, our first formatted string. We tell print() that it's a formatted
        # string using "f" right before the opening quotation marks. (Note that
        # this works in all strings, not just print().) From there, we use
        # braces around variable names and the rest is just plain text. The
        # braces in a formatted string basically say, "this is a bit of code."
        return f"{self.first_name} {self.middle_initial}. {self.last_name}"

    def display(self):
        """Display the information about the Person."""
        if not self.is_valid():
            print("Not a valid instance.")
            return

        # This is just getting the length of the longest bit of info, the
        # marriage status.
        marriage_status = "Marriage status:"
        length = len(marriage_status)

        # Print the formatted name from get_name().
        print(self.get_name())

        # And here ljust stands for "left justification". So we wrap
        # 'Age:'.ljust(length) in braces because we are adding extra spaces to
        # the end of 'Age:', enough to pad it to the same length as marriage
        # status. You'll also notice that the inner quotes are single quotes;
        # this is because they need to be a different type of quotation mark
        # from what's wrapping around the whole print statement. Single quotes
        # and double quotes have the same meaning in Python.
        print(f"{'Age:'.ljust(length)} {self.age}")
        print(f"{'Address:'.ljust(length)} {self.address}")

        # Here we have another bit of code, an inline if-else statement. If
        # John Smith is married (self.married == True) then we will print
        # "Married", otherwise "Unmarried".
        print(f"{marriage_status} {'Married' if self.married else 'Unmarried'}")

        # We'll only print John Smith's spouse information if he's married.
        if self.married:
            print(f"{'Spouse:'.ljust(length)} {self.spouse['first_name']} "
                  f"{self.spouse['middle_initial']}. {self.spouse['last_name']} "
                  f"({self.spouse['maiden_name']})")

        # And we'll only print his children if he has any.
        if len(self.children) > 0:
            print("Children:")
            for child in self.children:
                print("    " + child)


class Menu:
    # Here's the enum from earlier. Notice that Main, Change, and MarriageStatus
    # are set to 0, 1, and 2: this is because behind the scenes, they are
    # integers, but we can call them using their names! Basically, it's a fancy
    # wrapper for integer variables that denote a specific type.
    class Page(Enum):
        Main = 0
        Change = 1
        MarriageStatus = 2

    def __init__(self):
        """Initialize the Menu."""
        # We need to use the enum by calling its parent class, even though that
        # parent class is the current one. That's why we use "self": without
        # "self", the code actually has no idea what class it's part of.
        self.page = Menu.Page.Main

    def display(self):
        """Display the menu and return the input."""
        print()

        # We're using the enum here to check which page is being displayed:
        # if it's Menu.Page.Main, then display the main page; if it's anything
        # else, display the subpage. We can have more than two menu pages, in
        # which case we would need more than if-else.
        if self.page == Menu.Page.Main:
            print("What do you want to do?")
            print("1) Display information")
            print("2) Change information")
            print("3) Quit")
        elif self.page == Menu.Page.Change:
            print(f"What do you want to change?")
            print("1) First name")
            print("2) Middle initial")
            print("3) Last name")
            print("4) Age")
            print("5) Address")
            print("6) Marriage status")
            print("7) Add child")
            print("8) Back")
        else:
            print("1) Married")
            print("2) Unmarried")

        # The text inside the input() call is what will be displayed to the user
        # as a prompt. The ">" gives it an old-school terminal feeling, while
        # letting the user know that the program is waiting for input.
        return input("> ")


def main():
    # Here, we create a new argument parser instance for the command line.
    parser = argparse.ArgumentParser()
    # Then we add a required positional argument named "file". It is the first
    # argument provided after the Python execution command.
    parser.add_argument("file", type=str, help="file to load")

    # Here we parse the arguments given on the command line, then we can access
    # them via "args.argumentname".
    args = parser.parse_args()

    # Creating a new Person from our provided file, then loading the information
    # from that file.
    john_smith = Person(args.file)
    john_smith.load()

    # Creating a new menu object.
    menu = Menu()

    # This is used in a while loop to determine whether the user has asked to
    # quit the program or not.
    quit = False

    while not quit:
        # Since we get the input in the menu.display() function, we must assign
        # it to a variable to use it.
        command = menu.display()

        # Unfortunately, Python doesn't have switch statements and alternatives
        # are too new to rely on unless you know the target computer has the
        # latest version of Python.
        if menu.page == Menu.Page.Main:
            if command == "1":
                john_smith.display()
                pass
            elif command == "2":
                menu.page = Menu.Page.Change
                pass
            elif command == "3":
                # If the user enters "3" on the main menu, let them quit by
                # setting quit to True.
                quit = True
            else:
                print("Invalid command. Please try again.")
        else:
            if command == "1":
                john_smith.first_name = input("First name: ")
            elif command == "2":
                john_smith.middle_initial = input("Middle initial: ")
            elif command == "3":
                john_smith.last_name = input("Last name: ")
            elif command == "4":
                john_smith.age = input("Age: ")
            elif command == "5":
                john_smith.address = input("Address: ")
            elif command == "6":
                print(f"What is {john_smith.get_name()}'s marriage status?")

                invalid = True
                menu.page = Menu.Page.MarriageStatus

                while invalid:
                    command = menu.display()

                    if command == "1":
                        john_smith.married = True
                        invalid = False
                    elif command == "2":
                        john_smith.married = False
                        invalid = False
                    else:
                        print("Invalid marriage status. Please try again.")

                menu.page = Menu.Page.Change

                if not john_smith.married:
                    # Here we're going to ask the user for yes/no input. If the
                    # user does not enter "y" or "Y", then the spouse
                    # information will not be deleted. We should be ensuring
                    # that they enter y, n, yes, no, or any capitalization,
                    # but this is an example program.
                    command = input("Do you want to remove spouse information? "
                                    "(y/n) ")

                    if command.lower() == "y":
                        # We can get rid of the spouse information by just
                        # reinitializing person.spouse to an empty dictionary.
                        john_smith.spouse = {}
            elif command == "7":
                # Just like in our example file, here we're going to use
                # append() to add a child to the person's children.
                john_smith.children.append(input("Child's name: "))
            elif command == "8":
                # To go back to the main menu, we just set the current menu page
                # to Menu.Page.Main.
                menu.page = Menu.Page.Main
            else:
                print("Invalid command. Please try again.")

    command = input("Save before quitting? (y/n) ")

    # This will only save the changed information back to the person's file if
    # yes. If you make a mistake, you can exit and reopen the program to get
    # back the original file.
    if command.lower() == "y":
        john_smith.save()


# And here's the magic code to begin the program by calling the main() function.
if __name__ == "__main__":
    main()
