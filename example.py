'''
This is a Python Basics file for the CS300 term project. This is a Python
multi-line comment.

Python contains most of the features of C++ in a simpler package. Let's go
over some differences.
 * C++ requires manual memory management. Python has a garbage collector that
   will usually free memory when a variable is released.
 * Python does not use braces around most scopes and instead relies on
   indentation.
 * Python does not use semicolons at the end of lines. New lines are considered
   new statements, except in some cases such as multiline comments or within
   array and dictionary brackets.
 * Python is a "dynamically typed" language: variable types and functions are
   determined at runtime based on the data stored; you do not typically define
   types in the code.
 * Python does not have "pass by reference"; it uses "pass by assignment". This
   means that if a mutable object is passed into a function (e.g., a list), you
   can modify that object; if the variable is reassigned, the original object
   does not change. It's generally a good idea to return values from functions
   rather than attempt to modify a parameter. View this Stack Overflow answer
   for more details: https://stackoverflow.com/a/986145
 * In Python, functions must be defined before they can be called. Prototypes do
   not exist, and Python's method of "forward declaration" is simply to
   implement the function before it will be used.
 * Python does not have the ternary operator (?:) or pre/postfix increment and
   decrement operators (++ and --).
'''

# Let's start with libraries. Libraries are simple to import in Python:
import os                   # The os library allows us to read information about
                            # a user's computer such as the file system.
from os import path         # You can also import individual elements of a
                            # library.
import os.path as p         # Or import individual elements with an alias for
                            # easier access.
from pathlib import Path    # This is the actual library we'll be using to
                            # create paths for file reading and writing.


# To define a function, use "def" followed by the function name.
def my_func():
    # If the function does nothing, it should include the word "pass" to
    # indicate that it is empty and should be "passed" over.
    pass


# You can also include parameters/arguments.
def my_func2(arg1):
    pass


# One of the few times you may want to define a type explicitly is when you want
# to ensure a function receives only a certain data type.
def my_func3(arg1: str):
    pass


# Here is a function that takes two integer arguments named "x" and "y" then
# returns the sum of these two numbers. Note that functions are by default
# "void" unless a return statement is used.
def sum(x: int, y: int):
    # Also notice that there is a statement under the function name surrounded
    # by three sets of double quotes. This is called a "docstring", and it
    # documents the functionality of the method. In some text editors, it will
    # display this information to the user when they type or hover over the
    # function name. You should almost always include docstrings.
    # If you want to read more about docstring conventions, check out
    # https://www.python.org/dev/peps/pep-0257/
    """Return the sum of two numbers."""
    return x + y


# Here is a function that takes two integer arguments named "x" and "y" then
# returns the larger of the two numbers, or "y" if x == y.
def max(x: int, y: int):
    """Return the maximum of two numbers."""
    if x > y:
        return x
    else:
        return y


# Here is a function that "clamps" a number between two values.
def clamp(low: int, high: int, val: int):
    """Clamp a number between two values."""
    if val > high:
        return high
    elif val < low:
        return low
    else:
        return val


# And here is a function that returns whether two numbers are the same.
def equals(x: int, y: int):
    """Check if two numbers are equal to each other."""
    # Ideally, just return x == y, but this is for demonstration purposes.
    return x > y or x < y


# This function will be used to create the list that we will use for the rest of
# the examples.
def create_list():
    """Create a list of STEM subjects."""
    # Start by defining a list with one element. Lists are the default array
    # type in Python, and can contain multiple data types at once.
    my_list = ["Biology"]

    # Let's add another element with "append".
    my_list.append("Chemistry")

    # Let's add more than one element!
    my_list.extend(["Mathematics", "Physics", "Art"])

    # "Art" isn't a STEM pursuit!
    my_list.remove("Art")

    # Oops, we missed one... better insert it in the correct position.
    my_list.insert(1, "Computers")

    # It's "Computer Science", not "Computers".
    my_list.pop(1) # We can also omit the index to pop the last element.
    my_list.append("Computer Science")

    # Now it's out of order, so let's sort alphabetically.
    my_list.sort()

    # Add some garbage to index 3...
    my_list.insert(3, "a0uibgr")
    # And remove it by using Python's "slice" syntax to cut the list in half,
    # from index 0-3 and then 4 to the end (first index inclusive, last
    # exclusive).
    my_list = my_list[0:3] + my_list[4:]

    # Add some more garbage...
    my_list.extend(["asdguobn", "asduiogbnr", "abngao"])
    # And delete it again. This uses the slicing to remove the last three
    # elements, indicated by -3.
    del my_list[-3:]

    # Finally, let's return the list.
    return my_list


# This function will create the dictionary we'll be using for the other examples.
def create_dict():
    """Create a dictionary for John Smith and his family."""
    # First create the dictionary. Note that we can have multiple value types
    # and that we can have sublists and subdictionaries.
    my_dict = {
        "name_first": "Jon",
        "name_middle": "D",
        "name_last": "Smith",
        "spouse_name": "Jane Smith",
        "age": 34,
        "address": "1 Willow St.",
        "children": [
            "John Smith, Jr.",
            "Abby Smith",
            "Gregory Smith"
        ]
    }

    # We messed up John's name, so let's fix it.
    my_dict["name_first"] = "John"

    # John and his wife had another child last year, so let's add them.
    my_dict["children"].append("Sally Smith")

    # Jane should have her own dictionary entry, but for our purposes, we'll add
    # some extra data about her.
    # "del" will delete the entire key and its data from the dictionary.
    del my_dict["spouse_name"]

    # "spouse" is now a dictionary of its own!
    my_dict["spouse"] = {
        "name_first": "Jane",
        "name_middle": "B",
        "name_last": "Smith",
        "age": 38,
        "parents": [
            "Bobby Jones",
            "Betty Jones"
        ]
    }

    # And return it.
    return my_dict


# Let's go over loops. Python does not have do-while loops.
# This function prints the numbers from 1 to the input.
def while_loop(x: int):
    """Use a while loop to print from 1 to x."""
    # Like other languages, we must define our bounds outside the while loop.
    num = 1

    while num <= x:
        print(num)
        num += 1            # Note that Python does not have pre or postfix
                            # increment/decrement (++ or --).


# This for loop starts at 0 and ends at the input - 1.
def for_range(x):
    """Use a for loop to print from 0 to x."""
    # Note that the first value is inclusive and the second is exclusive, e.g.
    # if x = 10, then this will print 0 to 9.
    for i in range(0, x):
        print(i)

    # You can fix this by adding + 1 to the second value.
    for i in range(0, x + 1):
        print(i)


# This for loop starts at the first element in a list and prints the list.
def for_list(list):
    """Use a for loop to print each item in a list."""
    # You can loop through each item with a variable name.
    for item in list:
        print(item)

    # Or use len() to get the length of the list and use the index.
    for i in range(len(list)):
        print(list[i])


# This function will loop through a dictionary using a for loop.
def for_dict(dict):
    """Use a for loop to iterate over the keys and values in a dictionary."""
    # Loop through the keys and access values through indexing.
    # The same can be achieved with "for key in dict.keys()".
    for key in dict:
        print(key, ": ", dict[key])

    # Loop through the items in the dictionary as tuples.
    for item in dict.items():
        print(item)

    # Loop through only the values in the dictionary.
    for value in dict.values():
        print(value)


# This function will return only the values in list that start with the filter.
def filter_list(list, filter):
    """Filter a list to entries that start with filter."""
    # This is basically using a for loop. We name each item in the list "value",
    # then check if the value starts with the provided filter. The outer
    # brackets [] say that this is an array, while the inside acts as a for loop
    # and an if statement.
    return [value for value in list if value.startswith(filter)]


# This function will filter a dictionary to only the keys that start with the
# filter, then only the values that start with the filter. Then it will return
# both of these lists as a tuple.
def filter_dict(dict, key_filter, value_filter):
    """Filter a dictionary to lists with either the keys or values that start
    with filter."""
    key_dict = [key for key in dict if key.startswith(key_filter)]

    # Note that you can split this definition over multiple lines because it is
    # within the brackets. Also note that we need to use str() to convert the
    # value to a string here, because one of our values is an integer (age).
    value_dict = [value for value in dict.values()
                    if str(value).startswith(value_filter)]

    # The parentheses around these two variables indicate a tuple. This tuple's
    # values can be accessed via index, where tuple[0] = key_dict and
    # tuple[1] = value_dict.
    return (key_dict, value_dict)


# Time to learn how to read from a text file.
def read_file(filename):
    """Read from a text file."""
    # This creates a file "object" using the pathlib library.
    # The path will be at "./filename".
    file = Path(".") / filename

    # Let's first ensure the file exists.
    if not file.is_file():
        print("Invalid file.")
        return

    # The "with" statement opens a file within its scope. When the "with"
    # statement ends, the file automatically closes. Without "with", we would
    # have to manually close the file with f.close().
    # We're also going to open the file in read mode with 'r'.
    # 'r' = read
    # 'w' = write
    # 'a' = append
    # 'w+' = write and read
    with open(file, 'r') as f:
        # read() will read all the text in a file into a single string.
        # readlines() will read all lines from the file into a list of strings.
        read = f.read()
        # An internal line feed has moved from the beginning to the end of the
        # file as it read, so we need to reset it back to the beginning.
        f.seek(0)
        readlines = f.readlines()

        # Reset the feed again, then we can also read the file line-by-line.
        f.seek(0)
        for line in f:
            for_lines = []
            for_lines.append(line)

    # Now we're returning a 3-tuple!
    return (read, readlines, for_lines)


def write_file(filename):
    """Save data to a text file."""
    # Let's create the file object again. In reality, we would probably want to
    # store this value somewhere instead of creating it again, but these are
    # technically two "unrelated" functions so we'll do it twice.
    file = Path(".") / filename

    # If something exists with that name but is not a writeable file, let's
    # cancel.
    if file.exists() and not file.is_file():
        print("Invalid file.")
        return

    with open(file, 'w') as f:
        # First we're going to get some user input using the "input" function.
        # The text within the input() call is the prompt to display to the user.
        line = input("Enter some text: ")

        # Then we're going to write that text to the file as a single line.
        f.write(line)

        # Now I will repeat this question 10 times to create a list of strings.
        lines = []
      
        # We can use "string interpolation", or f-strings in Python, to insert
        # a variable into a string. Begin with the letter "f" before the opening
        # quotation mark, then wrap any referenced variables within curly
        # brackets {}.
        for i in range(10):
            lines.append(input(f"Enter some text ({i}): "))

        # For each line, let's add a line ending so that they will print
        # separately instead of in one block. You can modify each element in a
        # list easily using this syntax.
        lines = [line + "\n" for line in lines]

        # And then write all those lines to the file.
        f.writelines(lines)

    # Now go check out the file on the system to see what it says!
    # Note that this function changes the file as it goes, so if you interrupt
    # this function or the program crashes, the file will still be rewritten.
    # This can be good or bad depending on your use case, but if the user can
    # cancel input, it's usually a good idea not to write changes until they are
    # completely finished.


# Now let's go over classes.
# This is a class that does not use inheritance.
class MyClass:
    # Create a constructor (initializer). The constructor will always be named
    # "__init__".
    # Any function within a class must have its first parameter refer to the
    # class instance. This parameter is typically called "self", though it can
    # be named anything. This parameter is automatic and should never actually
    # be supplied when calling the function.
    def __init__(self):
        """Initialize the MyClass instance."""
        # Create an integer variable named "my_var" that belongs to the class.
        self.my_var = 1

        # Create a string variable named "my_other_var" that is local only to
        # this scope (the function).
        my_other_var = "Test"

        # Create an empty array variable.
        my_array = []

        # Create an empty dictionary variable. A dictionary can store any
        # type or amount of data like a class without a class definition.
        my_object = {}

        # Create a boolean variable that is equal to true. Note that Python
        # capitalizes "True" and "False".
        my_bool = True

        # Create an empty variable. "None" is equivalent to "null".
        my_null = None

    def my_class_func(self):
        """Print the value of my_var."""
        print(self.my_var)  # Print the class variable "my_var" to the console.


# This is a class derived from the earlier class MyClass.
class MyChild(MyClass):
    # The constructor takes three arguments. The first argument is the
    # automatic reference to the class instance; the second and third are user
    # provided.
    def __init__(self, first_name, last_name):
        """Initialize the MyChild instance."""
        # You need to explicitly call the parent's constructor. super() refers
        # only to the parent class, not the base class.
        super().__init__()
        # Now that the parent has been initialized, the child class can access
        # any members of the parent.
        print(self.my_var)

        # You can also pass in arguments and store them within the class.
        self.first_name = first_name
        self.last_name = last_name

        print(self.first_name)
        print(self.last_name)

    # Want to override a function? It's this simple. The function being called
    # is determined at runtime based on context. Note that the original function
    # in the parent class doesn't need the "virtual" keyword.
    def my_class_func(self):
        """Print an overridden statement."""
        print("Overridden!")


# This line is magical! It says if the current module's name is "__main__", then
# let's run this code. This is somewhat equivalent to C++'s "int main()", but
# you will need to run the program this way at the bottom of the main file.
# If you want, you can define a function then call it here to remove some of the
# functionality from the "if" statement.
if __name__ == "__main__":
    my_list = create_list()
    my_dict = create_dict()

    # Uncomment any of these if you want to see what the output is.
    # Sum:
    # print(sum(1, 5))
    # print(sum(2, 10))

    # Max:
    # print(max(1, 5))
    # print(max(5, 1))

    # Clamp:
    # print(clamp(0, 5, 2))
    # print(clamp(0, 5, -1))

    # Equals:
    # print(equals(1, 1))
    # print(equals(1, 2))

    # While:
    # while_loop(10)

    # For range:
    # for_range(10)
    # for_range("ABC")      # This will throw an error that we cannot use
                            # "range" on a string object.

    # For loop on a list:
    # for_list(my_list)

    # For loop on a dictionary:
    # for_dict(my_dict)

    # Filter a list:
    # print(filter_list(my_list, "C"))

    # Filter a dictionary:
    # print(filter_dict(my_dict, "a", "J"))

    # Read from a file:
    # print(read_file("lorem_ipsum.txt"))

    # Write to a file:
    # write_file("lorem_ipsum.txt")

    # MyClass:
    # my_class = MyClass()
    # my_class.my_class_func()

    # MyChild:
    # my_child = MyChild("John", "Smith")
    # my_child.my_class_func()

    # This isn't needed when any code is in the "if" statement body, but Python
    # will throw a fit if you haven't uncommented any of the above lines. It
    # will not affect functionality.
    pass


'''
This has been your Python crash course! Of course there's a ton more to learn,
and I can hopefully answer most other questions you'll have. We're going to put
it all together in a different file and make an actual working program! Go check
out my_program.py.
'''
