# Python Crash Course
Welcome to the non-comprehensive Python crash course! This is intended for students in the CS300 term project group who need some help learning Python before we begin.

Start with [example.py](example.py) for basic Python syntax as well as reading and writing to text files, then move on to [my_program.py](my_program.py) for JSON examples and data manipulation. Also check out [john_smith.json](john_smith.json) and [lorem_ipsum.txt](lorem_ipsum.txt) to see what kind of information you'll be loading. If you have any other questions, feel free to ask.

## A word of caution
Now that `example.py` reads and writes to a file, be careful! Don't enter any files that you don't want to lose data in, because they will likely be overwritten, even if you cancel the program (read the comments in the `write_file()` function in `example.py`).

## Directory of Concepts
<table>
    <tr>
        <th>example.py</th>
        <th>my_program.py</th>
    </tr>
    <tr valign="top">
        <td valign="top">
            <ol>
                <li><a href="example.py#L30">Importing libraries</a></li>
                <li><a href="example.py#L42">Basic function</a></li>
                <li><a href="example.py#L49">Function arguments</a></li>
                <li><a href="example.py#L55">Function arguments with type</a></li>
                <li><a href="example.py#L62">Adding two numbers</a></li>
                <li><a href="example.py#L76">If-else statements</a></li>
                <li><a href="example.py#L85">If-else if-else statements (elif)</a></li>
                <li><a href="example.py#L96">Or operator</a></li>
                <li><a href="example.py#L104">Lists</a></li>
                <li><a href="example.py#L147">Dictionaries</a></li>
                <li><a href="example.py#L194">While loops</a></li>
                <li><a href="example.py#L206">For loops in a range</a></li>
                <li><a href="example.py#L219">Looping through a list</a></li>
                <li><a href="example.py#L231">Looping through a dictionary</a></li>
                <li><a href="example.py#L248">Filtering a list</a></li>
                <li><a href="example.py#L260">Filtering a dictionary</a></li>
                <li><a href="example.py#L278">Reading a text file</a></li>
                <li><a href="example.py#L317">Writing to a text file</a></li>
                <li><a href="example.py#L359">Creating a class</a></li>
                    <ol>
                        <li><a href="example.py#L366">Class constructors (initializers)</a></li>
                        <li><a href="example.py#L389">Class functions</a></li>
                    </ol>
                <li><a href="example.py#L395">Inheriting classes (subclasses)</a></li>
                    <ol>
                        <li><a href="example.py#L403">Calling a parent class's constructor (initializer)</a></li>
                        <li><a href="example.py#L418">Overriding methods in a parent class</a></li>
                    </ol>
                <li><a href="example.py#L428">Starting the program</a></li>
            </ol>
        </td>
        <td>
            <ol>
                <li><a href="my_program.py#L12">Import statements</a></li>
                <li><a href="my_program.py#L27">Class constructor (initializer)</a></li>
                <li><a href="my_program.py#L49">Loading from a JSON file</a></li>
                <li><a href="my_program.py#L69">Saving to a JSON file</a></li>
                <li><a href="my_program.py#L97">Basic string/print formatting</a></li>
                <li><a href="my_program.py#L127">Advanced string/print formatting</a></li>
                <li><a href="my_program.py#L156">Enumerated types (enums)</a></li>
                <li><a href="my_program.py#L169">Printing a menu</a></li>
                <li><a href="my_program.py#L205">Prompting the user for input</a></li>
                <li><a href="my_program.py#L209">Parsing command line arguments</a></li>
                <li><a href="my_program.py#L227">The main program loop</a></li>
                <li><a href="my_program.py#L338">Starting the program</a></li>
            </ol>
        </td>
    </tr>
</table>

## Infrequently Asked Questions and Statements
### These files are long and scary.
Rest assured that a lot of that length is only whitespace and comments!

### I messed up a bunch of information in John Smith's file! How do I get it back?
Don't panic! Open the command line, `cd` into the project directory, and enter this command:
```bash
git checkout HEAD -- john_smith.json
```
That will reset the file back to the last commit. The same concept applies to `lorem_ipsum.txt`.

### Why can't I edit John Smith's spouse and children, but I can change his marital status?
Jane Smith and their children are entirely different people. In an ideal situation, we would have separate files on all of them and connect them via numeric IDs or another unique identifier. As it is, we're just going to prevent editing them and pretend that they're stored in separate files.
